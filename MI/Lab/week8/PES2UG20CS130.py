import numpy as np


class HMM:
    def __init__(self, A, states, emissions, pi, B):
        self.A = A
        self.B = B
        self.states = states
        self.emissions = emissions
        self.pi = pi
        self.N = len(states)
        self.M = len(emissions)
        self.make_states_dict()

    def make_states_dict(self):
        self.states_dict = dict(zip(self.states, list(range(self.N))))
        self.emissions_dict = dict(
            zip(self.emissions, list(range(self.M))))

    def viterbi_algorithm(self, seq):
        seq_len = len(seq)

        n_zeros = np.zeros((seq_len, self.N))
        temp = np.zeros((seq_len, self.N), dtype=int)

        for j in range(self.N):
            n_zeros[0, j] = self.pi[j] * self.B[j, self.emissions_dict[seq[0]]]
            temp[0, j] = 0

        for i in range(1, seq_len):
            for j in range(self.N):
                n_max = -1
                tempmax = -1
                for k in range(self.N):
                    localNu = n_zeros[i - 1, k] * self.A[k, j] * self.B[j, self.emissions_dict[seq[i]]]
                    if localNu > n_max:
                        n_max = localNu
                        tempmax = k
                n_zeros[i, j] = n_max
                temp[i, j] = tempmax

        n_max = -1
        tempmax = -1

        for j in range(self.N):
            localNu = n_zeros[seq_len - 1, j]
            if localNu > n_max:
                n_max = localNu
                tempmax = j
        states = [tempmax]

        for i in range(seq_len - 1, 0, -1):
            states.append(temp[i, states[-1]])
        states.reverse()

        self.states_dict = {v: k for k, v in self.states_dict.items()}
        return [self.states_dict[i] for i in states]