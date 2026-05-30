from correlation.scorer import Scorer

s = Scorer()

host = "admin.graphql.example.com"

score = s.score(host)

severity = s.severity(score)

print(host)
print(score)
print(severity)