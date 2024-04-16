
import numpy as np

states = ['state1', 'state2', 'state3', 'state4']
actions = ['action1', 'action2', 'action3', 'action4']
rewards = np.array['reward1', 'reward2', 'reward3', 'reward4'];
transitions =np.array([[[0.7, 0.3], [0.4, 0.6]], [[0.6, 0.4], [0.3, 0.7]], [[0.5, 0.5], [0.2, 0.8]]])


#Simple Policy Evaluating formula

def evaluate_policy(policy, gamma=0.95, threshold=0.01):
    V = np.zeros(len(states))
    while True:
        V_prev = np.copy(V)
        for s in range(len(states)):
            a = policy[s]
            V[s] = sum([transitions[s][a][s_prime] * (rewards[s][a] + gamma * V_prev[s_prime])  for s_prime in range(len(states))])
        if np.sum(np.fabs(V - V_prev)) < threshold:
            break

        return V


policy = [0, 1, 1]
V = evaluate_policy(policy)
print("Policy Evaluation level: ")

# but how can i evaluate policy level?

#Let`s find this coding`s optimization and weak part, be more clever.