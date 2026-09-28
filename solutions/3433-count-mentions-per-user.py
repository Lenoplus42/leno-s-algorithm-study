class Solution:
    def countMentions(
        self, numberOfUsers: int, events: list[list[str]]
    ) -> list[int]:
        events = sorted(
            events, key=lambda e: (int(e[1]), e[0] == "MESSAGE")
        )
        mentions = [0] * numberOfUsers
        online_at = [0] * numberOfUsers

        for kind, timestamp, content in events:
            t = int(timestamp)
            if kind == "OFFLINE":
                online_at[int(content)] = t + 60
            elif content == "ALL":
                for user in range(numberOfUsers):
                    mentions[user] += 1
            elif content == "HERE":
                for user in range(numberOfUsers):
                    if t >= online_at[user]:
                        mentions[user] += 1
            else:
                for token in content.split():
                    mentions[int(token[2:])] += 1

        return mentions
