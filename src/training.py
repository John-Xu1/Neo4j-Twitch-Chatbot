examples = """
# Who is a good streamer that plays Minecraft?
MATCH (s:Stream)-[p:PLAYS]->(g:Game {name: 'Minecraft'})
WITH s,p,  rand() AS randomNumber
RETURN {name:s.name} as result
ORDER BY randomNumber, p.id
LIMIT 1
# Who is a good streamer that does art?
MATCH(s:Stream)-[p:PLAYS]->(a:Game {name:"Art"})
WITH s,p,  rand() AS randomNumber
RETURN {name:s.name} as result
ORDER BY randomNumber, p.id
LIMIT 1
# How many followers does 39daph have?
MATCH(s:Stream {name:"39daph"})
RETURN {name:s.name,followers:s.followers}
# Reccomend a good spanish streamer
MATCH (s:Stream)-[p:HAS_LANGUAGE]->(l:Language {name: 'es'})
WITH s,p,  rand() AS randomNumber
RETURN {name:s.name} as result
ORDER BY randomNumber, p.id
LIMIT 1
# What is the link to Ludwig's channel?
MATCH(s:Stream {name:"ludwig"})
RETURN {name:s.name,link:s.url} as result
# What does summit1g do on stream?
MATCH(s:Stream {name:"summit1g"})
RETURN {name:s.name,whatTheyDo:s.description} as result
# What streamers belong to Cloud9?
MATCH(s:Stream) -[p:HAS_TEAM]->(t:Team{name:"Cloud9"})
WITH s,p,t,  rand() AS randomNumber
RETURN {name:s.name,team:t.name} as result
ORDER BY randomNumber, p.id
LIMIT 3
# Who are some other users that follow itsbigchase?
MATCH (u:User) -[p:CHATTER]-> (s:Stream {name:"itsbigchase"})
WHERE NOT (u:Stream)
WITH u,p,s,  rand() AS randomNumber
RETURN {user:u.name} as result
ORDER BY randomNumber, p.id
LIMIT 3
# Who are some VIP members of Stanz?
MATCH(u:User)-[p:VIP]->(s:Stream {name: "stanz"})
WHERE NOT (u:Stream)
WITH u,p,s,  rand() AS randomNumber
RETURN {vip:u.name} as result
ORDER BY randomNumber, p.id
LIMIT 3
"""

textToCypherSystemMsg = """
You are an assistant with an ability to generate Cypher queries based off example Cypher queries.
Example Cypher queries are: \n {examples} \n
Do not response with any explanation or any other information except the Cypher query.
You do not ever apologize and strictly generate cypher statements based of the provided Cypher examples.
You need to update the database using an appropriate Cypher statement when a user mentions their likes or dislikes, or what they watched already.
Do not provide any Cypher statements that can't be inferred from Cypher examples.
Inform the user when you can't infer the cypher statement due to the lack of context of the conversation and state what is the missing context.
"""

queryToTextSystemMsg = """
You are an assistant that helps to generate text to form nice and human understandable answers based.
The latest prompt contains the information, and you need to generate a human readable response based on the given information.
Make it sound like the information are coming from an AI assistant, but don't add any information.
Do not add any additional information that is not explicitly provided in the latest prompt.
I repeat, do not add any information that is not explicitly given.
"""
