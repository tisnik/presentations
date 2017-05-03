
Agents
------

(def my-agent (agent 0))

(send my-agent + 6)

(send my-agent * 7)

@my-agent


(def agent1 ....
...send slow computation
(def agent2 ....
...send slow computation
(await agent1 agent2)
