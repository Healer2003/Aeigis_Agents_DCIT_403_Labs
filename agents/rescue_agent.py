from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
import asyncio

class RescueAgent(Agent):
    class TaskBehaviour(CyclicBehaviour):
        async def run(inner_self):
            msg = await inner_self.receive(timeout=5)
            if msg:
                print(f"RescueAgent received request: {msg.body}")
                await asyncio.sleep(3)
                print("RescueAgent completed task")

        
                inform_msg = Message(to="coordinator@xmpp.jp")
                inform_msg.set_metadata("performative", "inform")
                inform_msg.body = f"Completed task: {msg.body}"
                await inner_self.send(inform_msg)
                print("RescueAgent informed Coordinator of completion")

    async def setup(self):
        self.add_behaviour(self.TaskBehaviour())

async def main():
    agent = RescueAgent("rescueagent47@xmpp.jp", "123456")
    await agent.start()
    try:
        while agent.is_alive():
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())