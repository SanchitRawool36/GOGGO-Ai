from runtime.agents.agent_manager import AgentManager
from runtime.tasks.task import Task

class Collaboration:

    def __init__(self):
        self.manager = AgentManager()

    def execute(self, task: Task):
        # Step 1: CEO delegates the task to the CTO
        ceo = self.manager.get("CEO")
        
        prompt_ceo_delegate = f"""
You are the CEO. Your role is to provide clear, high-level direction.

Delegate the following task to the CTO. Be concise and focus on the "what," not the "how."

Task: {task.title}
Description: {task.description}
"""
        delegation = ceo.run(prompt_ceo_delegate)
        print("--- CEO Delegation ---")
        print(delegation)

        # Step 2: CTO executes the task
        cto = self.manager.get("CTO")
        
        prompt_cto_execute = f"""
As the CTO, you are responsible for the technical execution of tasks.

CEO's Instruction:
{delegation}

Complete this task. Provide a technical implementation or a detailed plan.

Task: {task.title}
Description: {task.description}
"""
        result = cto.run(prompt_cto_execute)
        print("\n--- CTO Execution ---")
        print(result)

        # Step 3: HR reviews the work for clarity and professionalism
        hr = self.manager.get("HR")
        
        prompt_hr_review = f"""
You are the HR Manager. Your role is to ensure inter-departmental communication is clear, professional, and constructive.

Review the completed work from the CTO. Focus on clarity, tone, and potential for improvement in collaboration, not the technical details.

Task: {task.title}
CTO's Output:
{result}

Provide brief, actionable feedback for improvement.
"""
        review = hr.run(prompt_hr_review)
        print("\n--- HR Review ---")
        print(review)

        # Step 4: CEO gives final approval
        prompt_ceo_approve = f"""
As the CEO, you make the final decision.

Based on the CTO's work and HR's review, decide whether to approve or reject the completed task. Your decision should be brief and clear.

CTO's Output:
{result}

HR's Review:
{review}

Approve or Reject?
"""
        approval = ceo.run(prompt_ceo_approve)
        print("\n--- CEO Final Approval ---")
        print(approval)

        # Step 5: Mark task as COMPLETED if approved
        if "approve" in approval.lower():
            task.status = "COMPLETED"
            print(f"\n--- Task Status ---")
            print(task.status)
        else:
            task.status = "REJECTED"
            print(f"\n--- Task Status ---")
            print(task.status)
