#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from yt_consultant.crew import YtConsultant

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Social Engineering, Politics, Economics, History',
        'channel_name': 'Ferry Irwandi',
        'channel_url': 'https://www.youtube.com/@FerryIrwandi',
        'country': 'Indonesia',
        'category': 'Social Education',
        

    }
    
    try:
        YtConsultant().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()
