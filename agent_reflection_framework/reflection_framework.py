import autogen


# Configuration for LLM model
class LLMConfig:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model


# Base class for all agents
class Agent:
    def __init__(self, name, system_message, llm_config):
        self.name = name
        self.system_message = system_message
        self.llm_config = llm_config
        self.agent = autogen.AssistantAgent(
            name=self.name,
            system_message=self.system_message,
            llm_config=self.llm_config.__dict__,
        )

    def generate_reply(self, task):
        return self.agent.generate_reply(messages=[{"content": task, "role": "user"}])


# Writer Agent
class WriterAgent(Agent):
    def __init__(self, llm_config):
        system_message = (
            "You are a writer. You write engaging and concise blogposts (with title) "
            "on given topics. You must polish your writing based on the feedback you receive "
            "and give a refined version. Only return your final work without additional comments."
        )
        super().__init__("Writer", system_message, llm_config)


# Critic Agent
class CriticAgent(Agent):
    def __init__(self, llm_config):
        system_message = (
            "You are a critic. You review the work of the writer and provide constructive "
            "feedback to help improve the quality of the content."
        )
        super().__init__("Critic", system_message, llm_config)

    def register_nested_chats(self, review_chats, trigger_agent):
        self.review_chats = review_chats
        self.trigger_agent = trigger_agent

    def initiate_chat(self, task):
        # Simulate interaction with the writer and nested chats with reviewers
        for review in self.review_chats:
            recipient = review["recipient"]
            recipient.generate_reply(task)  # This would invoke the reviewer's feedback
        return "Feedback Aggregated"


# Reviewer Agent (SEO, Legal, Ethics)
class ReviewerAgent(Agent):
    def __init__(self, name, llm_config, role_description):
        system_message = (
            f"You are a {name.lower()} reviewer, known for your ability to {role_description}. "
            "Make sure your suggestion is concise (within 3 bullet points), concrete and to the point. "
            "Begin the review by stating your role."
        )
        super().__init__(name, system_message, llm_config)


# Meta Reviewer Agent
class MetaReviewerAgent(Agent):
    def __init__(self, llm_config):
        system_message = (
            "You are a meta reviewer, you aggregate and review the work of other reviewers "
            "and give a final suggestion on the content."
        )
        super().__init__("Meta Reviewer", system_message, llm_config)

    def aggregate_feedback(self, feedbacks):
        return {"final_suggestion": "Final feedback aggregated: " + str(feedbacks)}


# Task Definition
class BlogPostTask:
    def __init__(self, topic="DeepLearning.AI", word_limit=150):
        self.task = (
            f"Write a concise but engaging blogpost about {topic}. Make sure the blogpost is "
            f"within {word_limit} words."
        )


# Reflection Message Helper
def reflection_message(recipient, messages, sender, config):
    return f'''Review the following content.\n\n {recipient.chat_messages_for_summary(sender)[-1]['content']}'''


# Main Orchestration (Execution)
def main():
    # LLM Configuration
    llm_config = LLMConfig()

    # Instantiate Agents
    writer = WriterAgent(llm_config)
    critic = CriticAgent(llm_config)

    seo_reviewer = ReviewerAgent("SEO Reviewer", llm_config, "optimize content for search engines")
    legal_reviewer = ReviewerAgent("Legal Reviewer", llm_config, "ensure content is legally compliant")
    ethics_reviewer = ReviewerAgent("Ethics Reviewer", llm_config, "ensure content is ethically sound")
    meta_reviewer = MetaReviewerAgent(llm_config)

    # Define the task
    task = BlogPostTask()

    # Writer generates the blog post
    writer_reply = writer.generate_reply(task.task)
    print(f"Writer's Reply:\n{writer_reply}\n")

    # Critic Agent initiates nested chats with reviewers
    review_chats = [
        {"recipient": seo_reviewer, "message": reflection_message, "max_turns": 1},
        {"recipient": legal_reviewer, "message": reflection_message, "max_turns": 1},
        {"recipient": ethics_reviewer, "message": reflection_message, "max_turns": 1},
        {"recipient": meta_reviewer,
         "message": "Aggregate feedback from all reviewers and give final suggestions on the writing.", "max_turns": 1},
    ]

    # Register nested chats
    critic.register_nested_chats(review_chats, trigger_agent=writer)

    # Critic agent initiates the review process
    critic_feedback = critic.initiate_chat(task.task)
    print(f"Critic's Feedback:\n{critic_feedback}\n")

    # Aggregating feedback from all reviewers
    final_feedback = meta_reviewer.aggregate_feedback([
        {"Reviewer": "SEO Reviewer", "Review": "Optimize keyword usage."},
        {"Reviewer": "Legal Reviewer", "Review": "Ensure no copyright violations."},
        {"Reviewer": "Ethics Reviewer", "Review": "Check ethical guidelines compliance."}
    ])

    print(f"Final Feedback from Meta Reviewer:\n{final_feedback['final_suggestion']}")


if __name__ == "__main__":
    main()
