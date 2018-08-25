import time


class SolutionDP(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        S = [None] * K
        for i in range(0, K):
            S[i] = [None] * N
        S[0] = range(1, N + 1)
        for k in range(1, K):
            for f in range(0, N):
                S[k][f] = 1

        for k in range(1, K):
            for f in range(k, N):
                S[k][f] = f
                for i in range(0, f):
                    out_breaks = 0
                    out_dn_break = 0
                    if i > 0:
                        out_breaks = S[k - 1][i - 1]
                    if i < f:
                        out_dn_break = S[k][f - i - 1]
                    S[k][f] = min(S[k][f], 1 + max(out_breaks, out_dn_break))

        return S[K - 1][N - 1]


class SolutionDPBinSearchBottomUp(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 1

        S = [None] * K
        for i in range(0, K):
            S[i] = [None] * N
        S[0] = range(1, N + 1)
        for k in range(1, K):
            S[k][0] = 1

        for k in range(1, K):
            for f in range(1, N):
                S[k][f] = f + 1
                low, high = 0, f - 1
                while (low + 1) < high:
                    i = (low + high) / 2
                    out_breaks = 0
                    out_dn_break = 0
                    if i > 0:
                        out_breaks = S[k - 1][i - 1]
                    if i < f:
                        out_dn_break = S[k][f - i - 1]
                    if out_breaks > out_dn_break:
                        high = i
                    if out_breaks < out_dn_break:
                        low = i
                    else:
                        high = i

                for i in [low, high]:
                    out_breaks = 0
                    out_dn_break = 0
                    if i > 0:
                        out_breaks = S[k - 1][i - 1]
                    if i < f:
                        out_dn_break = S[k][f - i - 1]
                    S[k][f] = min(S[k][f], 1 + max(out_breaks, out_dn_break))
        return S[K - 1][N - 1]


class SolutionDPBinSearchTopDown(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        def F(K, N, S):
            if N == 0:
                return 0
            if K == 1:
                return N
            if N == 1:
                return 1

            if (K, N) not in S:
                low = 1
                high = N
                while high > (low + 1):
                    mid = (low + high) / 2
                    out_breaks = F(K - 1, mid - 1, S)
                    out_dn_break = F(K, N - mid, S)
                    if out_breaks > out_dn_break:
                        high = mid
                    elif out_breaks < out_dn_break:
                        low = mid
                    else:
                        high = low = mid
                S[K, N] = 1 + min([
                    max(F(K - 1, i - 1, S), F(K, N - i, S))
                    for i in (low, high)
                ])

            return S[K, N]

        S = dict()
        return F(K, N, S)


class SolutionDPBinSearchBottomUp2(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 1
        if K == 1:
            return N

        dp_prev_k = range(0, N + 1)
        for k in range(2, K + 1):
            dp_cur_k = [None] * (N + 1)
            dp_cur_k[0] = 0
            n_min = 1
            for n in range(1, N + 1):
                f1 = max(dp_prev_k[n_min - 1], dp_cur_k[n - n_min])
                f2 = max(dp_prev_k[n_min], dp_cur_k[n - n_min - 1])
                while n_min < n and f1 > f2:
                    n_min += 1
                    f1 = max(dp_prev_k[n_min - 1], dp_cur_k[n - n_min])
                    f2 = max(dp_prev_k[n_min], dp_cur_k[n - n_min - 1])
                dp_cur_k[n] = 1 + f1
            dp_prev_k = dp_cur_k

        return dp_cur_k[-1]
