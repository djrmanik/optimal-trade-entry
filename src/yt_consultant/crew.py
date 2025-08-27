from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field

class YoutubeChanelResearch(BaseModel):
    channel_name: str = Field(description="The name of the YouTube channel")
    channel_url: str = Field(description="The URL of the YouTube channel")
    subscribers: str = Field(description="The number of subscribers the channel has")
    total_videos: str = Field(description="The total number of videos on the channel")
    total_views: str = Field(description="The total number of views the channel has")
    description: str = Field(description="A brief description of the channel")
    country: str = Field(description="The country where the channel is based")
    category: str = Field(description="The category of the channel (e.g., Education, Entertainment, etc.)")
    top_videos: List[str] = Field(description="A list of the top 5 videos on the channel with their titles and URLs")

class YoutubeChannelResearchList(BaseModel):
    channels: List[YoutubeChanelResearch] = Field(description="A list of YouTube channel research results")

@CrewBase
class YtConsultant():
    """YtConsultant crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def youtube_top_channel_researcher(self) -> Agent:
        """Agent that researches top YouTube channels"""
        return Agent(
            config=self.agents_config['youtube_top_channel_researcher'],
            tools=[SerperDevTool()],
            verbose=True
        )
    
    @agent
    def youtube_channel_analyst(self) -> Agent:
        """Agent that analyzes YouTube channels"""
        return Agent(
            config=self.agents_config['youtube_channel_analyst'],
            verbose=True
        )
    
    @agent
    def youtube_channel_consultant(self) -> Agent:
        """Agent that provides consulting on YouTube channels"""
        return Agent(
            config=self.agents_config['youtube_channel_consultant'],
            verbose=True
        )
    
    @task
    def research_top_channel_researcher_task(self) -> Task:
        """Task to research top YouTube channels"""
        return Task(
            config=self.tasks_config['youtube_top_channel_researcher_task'],
            output_pydantic=YoutubeChannelResearchList
        )
    
    @task
    def youtube_channel_analyst_task(self) -> Task:
        """Task to analyze YouTube channels"""
        return Task(
            config=self.tasks_config['youtube_channel_analyst_task'],
        )
    
    @task
    def youtube_channel_consultant_task(self) -> Task:
        """Task to provide consulting on YouTube channels"""
        return Task(
            config=self.tasks_config['youtube_channel_consultant_task'],
        )
    
    @crew
    def crew(self) -> Crew:
        """Define the crew process"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )


