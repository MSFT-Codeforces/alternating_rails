#include <iostream>
#include <unordered_set>
#include <cstdint>
#include <chrono>
#include <algorithm>

using namespace std;

struct State {
    long long x;
    long long y;

    bool operator==(const State &other) const {
        return x == other.x && y == other.y;
    }
};

/*
    SplitMix64 hash: standard technique to get a robust hash for unordered_set.
    This is not an "algorithmic optimization" for the problem itself; it just
    helps the brute-force baseline avoid pathological hashing behavior.
*/
static uint64_t splitmix64(uint64_t x) {
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
}

struct StateHash {
    size_t operator()(const State &s) const {
        static const uint64_t fixedRandom =
            (uint64_t)chrono::steady_clock::now().time_since_epoch().count();

        uint64_t hx = splitmix64((uint64_t)s.x + fixedRandom);
        uint64_t hy = splitmix64((uint64_t)s.y + fixedRandom + 0x9e3779b97f4a7c15ULL);

        // Combine hashes.
        uint64_t h = hx ^ (hy + 0x9e3779b97f4a7c15ULL + (hx << 6) + (hx >> 2));
        return (size_t)h;
    }
};

/*
    Brute-force baseline:
    - Simulate tick by tick.
    - Maintain the full set of reachable (x, y) states after at most i ticks.
      (Because choosing d = 0 allows "waiting", reachability is monotone in time.)
    - On tick i, enumerate all possible distances d = 0..min(K,i) and update
      the corresponding coordinate depending on parity of i.
    - Discard any move that would overshoot X or Y (since movement is only
      non-decreasing, overshooting can never be repaired).

    This is intentionally non-optimal and intended only for small/medium cases.
*/
static long long bruteForceMinTicks(long long xTarget, long long yTarget, long long k) {
    if (xTarget == 0 && yTarget == 0) {
        return 0;
    }

    unordered_set<State, StateHash> prevStates;
    unordered_set<State, StateHash> nextStates;

    prevStates.insert(State{0, 0});

    for (long long tick = 1; ; tick++) {
        // Choosing d = 0 keeps all previous states reachable.
        nextStates = prevStates;

        long long maxStep = min(k, tick);

        if (tick % 2 == 1) {
            // Odd tick: move east (increase X)
            for (const State &s : prevStates) {
                long long remaining = xTarget - s.x;
                if (remaining <= 0) {
                    continue;
                }
                long long limit = min(maxStep, remaining);
                for (long long d = 1; d <= limit; d++) {
                    nextStates.insert(State{s.x + d, s.y});
                }
            }
        } else {
            // Even tick: move north (increase Y)
            for (const State &s : prevStates) {
                long long remaining = yTarget - s.y;
                if (remaining <= 0) {
                    continue;
                }
                long long limit = min(maxStep, remaining);
                for (long long d = 1; d <= limit; d++) {
                    nextStates.insert(State{s.x, s.y + d});
                }
            }
        }

        if (nextStates.find(State{xTarget, yTarget}) != nextStates.end()) {
            return tick;
        }

        prevStates.swap(nextStates);
        nextStates.clear();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        long long x, y, k;
        cin >> x >> y >> k;
        cout << bruteForceMinTicks(x, y, k) << "\n";
    }

    return 0;
}