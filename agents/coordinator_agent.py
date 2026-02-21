from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template
import asyncio

class CoordinatorAgent(Agent):
    class ListenBehaviour(CyclicBehaviour):
        async def run(inner_self):
            msg = await inner_self.receive(timeout=5)
            if msg:
                print(f"Coordinator received: {msg.body}")

                # Send request to RescueAgent
                request_msg = Message(to="rescue@xmpp.jp")
                request_msg.set_metadata("performative", "request")
                request_msg.body = f"Respond to: {msg.body}"
                await inner_self.send(request_msg)
                print("Coordinator sent request to RescueAgent")

    async def setup(self):
        print(f"{self.jid} starting...")
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(self.ListenBehaviour(), template)

async def main():
    agent = CoordinatorAgent("coordinator@xmpp.jp", "pass1234")
    await agent.start()
    try:
        while agent.is_alive():
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())