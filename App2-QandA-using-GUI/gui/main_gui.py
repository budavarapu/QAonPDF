import tkinter as tk
from tkinter import filedialog, messagebox
import threading
from app.pdf_extractor import extract_text_from_pdf
from app.question_answering import get_answers_from_text
from app.slack_integration import post_answers_to_slack
import os

class PDFQAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Question and Answering App")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Select a PDF file:")
        self.label.pack()

        self.select_button = tk.Button(self.root, text="Select PDF", command=self.select_pdf)
        self.select_button.pack()

        self.questions_label = tk.Label(self.root, text="Enter questions (comma-separated):")
        self.questions_label.pack()

        self.questions_entry = tk.Entry(self.root, width=50)
        self.questions_entry.pack()

        self.slack_channel_label = tk.Label(self.root, text="Enter Slack channel (e.g., #general):")
        self.slack_channel_label.pack()

        self.slack_channel_entry = tk.Entry(self.root, width=50)
        self.slack_channel_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.pack()

        self.progress_label = tk.Label(self.root, text="")
        self.progress_label.pack()

    def select_pdf(self):
        self.pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.pdf_path:
            self.label.config(text=f"Selected file: {self.pdf_path}")

    def submit(self):
        if not hasattr(self, 'pdf_path'):
            messagebox.showerror("Error", "Please select a PDF file.")
            return

        questions = self.questions_entry.get()
        if not questions:
            messagebox.showerror("Error", "Please enter questions.")
            return

        slack_channel = self.slack_channel_entry.get()
        if not slack_channel:
            messagebox.showerror("Error", "Please enter a Slack channel.")
            return

        questions_list = [q.strip() for q in questions.split(',')]

        thread = threading.Thread(target=self.process_pdf, args=(self.pdf_path, questions_list, slack_channel))
        thread.start()

    def process_pdf(self, pdf_path, questions, slack_channel):
        self.progress_label.config(text="Processing...")

        try:
            text = extract_text_from_pdf(pdf_path)

            openai_api_key = os.getenv('OPENAI_API_KEY')
            answers = get_answers_from_text(text, questions, openai_api_key)

            slack_token = os.getenv('SLACK_TOKEN')
            post_answers_to_slack(answers, slack_token, slack_channel)

            self.progress_label.config(text="Done! Answers posted to Slack.")
        except Exception as e:
            self.progress_label.config(text=f"Error: {e}")

