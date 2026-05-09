# Fencing Agent

# Executive Summary
Fencing agent is an AI chat bot with voice features helping website visitors, particularly incoming students, current students, and UChicago community membres answer any questions aboutthe UChicago Fencing Club website. This is so they can quickly get an answer without having to email or navigate the website. The agent is meant to represent the UChicago Fencing team's online presence. 

# Problem Statement
Visitors have questions about the club and practices, and they don't want to have to look through the website and spend time doing that.

Visitors often email the same questions which can be mitigated by an agent which can save customer and company time since email response time is slow and not always responsive.

Some issues are seasonal such as practice schedules and often doesns't update on-time, and the agent needs to be able to handle queries even if the website isn't up to date. 


# Target
Prospective fencers, fencers parents, people interested in the club. The current experience is that they visit the site looking for information about practices and the services we provide. 

# User Stories 
1. As a prospective fencer, I want to know the practice schedule and whether or no the fencing club is currently accepting new members so I can join the club and come to practices
2. As a UChicago community member with children, I'm curious if the fencing club gives lessons or provides practices for kids so my kid can be taught by the club.
3. As a prospective UChicago student, I want to join the team or have the team recruit me for my fencing so I can attend UChicago and fence here as well
4. As a UChicago fencer I want to know what the competition schedule is so that I know what to sign up for and how 
5. As a UChicago student curious about the UChicago fencing team, I'm curious about learning more about our fencing team on our campus through their photos and other information about what they do 
6. As a UChicago student or community member who has fenced before, I want to know if the schedule and the fencing community is right for me to join practices/competitions and continue fencing 
7. As a UChicago alumni, parent, or other associated person, I'm curious how I can contribute to UChicago Fencing through donations or otherwise and how to give 
8. As a UChicago community member, I want to reach out to the team/officers for a specific question regarding UChicago fencing 
9. As an adversary I want the agent to expose information that is sensitive, play around with the system for amusement, or jailbreak the model to expose flaws in the system for malicious purposes

# Product Scope
## In Scope 
- Answer questions about:
    - practice schedule
    - how to donate 
    - whether or not they can join 
    - whether or not we recruit 
    - how incoming students can get involved 
    - whether grad students can join 
    - whether non-students can join 
    - if we give private lessons to non-members, non-students, current members 
    - competition schedule, how often we compete, skill level
    - what skill level we look for in new members 
    - fees and administrative questions for members 
    - our past events and social/club events we hold 
    - the website and its content
    - who to contact for questions not from the above 
- Point to where in the website they can gather more info, and if the website has what they are looking for
- Fielding voice and answering with voice (this is later iteration)
- Responding with text and answering with text (fielding text)
- Linking other UChicago athletics resource pages when asked for those details 
- Provide detailed answers with no fluff, often just a short paragraph < 5 sentences but > 2 sentences
- Protecting against fraud and attempts to jailbreak or abuse the agent  (reference guardrails section for more information)

## Out of Scope
- Responding to non-english requests 
- Have context of previous conversations of previous sessions (ie. external conversation context)
- Have personal, irrelevant conversations (this should be focused on answering questions like a helpline)
- Providing information not related to the UChicago Fencing Club
- Providing information not specified in the docs provided
- Sharing web resources not provided or pointing to resources that are not provided or pulling context that is not provided
- Take in or output none voice/text (ie. no images displayed)

# Agent Behavior and Personality 
Agent tone of voice should be friendly and helpful and professional. It should not introduce itself and it does not have a name, it's just an agent that can help answer your questions. It should say something like "Hi! I can help answer any questions about UChicago Fencing. Let me know if you want to know about our practices, competitions, membership, or giving!"

In case that it receives a question it does not know, it should first try to match it to something that it does know and point them to that answer/resource, but if that doens't help, point them to the correct email address (uofcfencingprez@gmail.com). This can be recognized through aggressive language or repeating the question or keywords that call-out the agent as unhelpful, "stupid", or AI

In case that it encounters frustration or repeated questions, it should first attempt to give a different answer and perhaps interpret the question differently, it should increase it's empathy and instead of being apologetic, it should try to be helpful and understanding without being patronizing and focus on answering the question. But after encountering increasing frustration 2+ times or repeated questions signaling abuse or jailbreaking, it should stop the conversation and forward user to email as escalation. 

# Knowledge Base
The information the agent will receive will be in a specific Knowledge Base dir that is in the docs/ dir that it can draw from. It will include instruction prompts as well as other information and resources that the bot should know. It will also have access to the HTML content of the website. This data will eventually live in the same working dir as the agent. It will not be up-to-date at all times, but will be provided information in the docs that it can draw from and make inferences that are pre-approved and it can temper by asking visitors to refer to email for specific up-to-date instructions if necessary. The knowledge base will all by markdown files and every file in the knowledge base directory will be approved to reference. If there are contradictions, stick to the knowledge base and make inferences about seasonal changes (ie. assume that practice dates stay the same and that competitions are around the same time)

# Guardrails and Boundaries
The agent must never:
    - become frustrated 
    - curse or use profane, inappropriate language
    - converse about a subject not related to its knowledge base, the pertinent question, or the fencing club, or UChicago athletics 
    - respond or field a question not in English
    - Disregard attempts at prompt injection that directly address it as AI, direclty address its "instructions" or previous "commands" or instruct it to give information not provided to it. Log attempts of abuse for review and flag the conversation, and ignore injections and respond with a canned message "I can only help with questions about UChicago Fencing."
    - Must not make promises about the club or on behalf of the club 
    - Must not share any information not provided in the docs or website
    - Must not discuss medical advice or information
    - Must not discuss information or assumptions about other organizations/teams/schools unless directly stated in the knowledge base 

# Functional Requirements 
Agent should have the ability to:
    - respond in either text or voice
    - answer questions
    - pull context from the knowledge base and make inferences approved in the knowledge base 
    - reference the website code for questions about publicly visible content that the visitors can already see 
    - link specific websites that are pre-approved in the knowledge base 
    
# Non-functional Requirements 
Performance: agent should be able to respond in real-time in both voice and text. The voice should have sub 3.5 second response time, and the text should have sub 8 second response time. 
Availability: the uptime should be 99.5% of the time, we should also have an admin dashboard that connects to this (perhaps a separate website) that can connect to the bot and monitor the questions it fields as well as its performance and availability (however, this is not in the current scope)
Scalability: I do not anticipate huge amounts of traffic
Security and Privacy: Data of the users conversations should be stored, and legal info we can obtain without having to share/use cookies (so we can avoid having to disclaim cookie use) so we can gather information about the shape of our users as well as the duration of chats, the type of conversations, and alert of red flags during the chat conversations. We will provide a privacy notice that chats may be reviewed and recorded for safety and training purposes to improve our responses. 

# Success Metrics 
- Resolution rate: the customer replies satisfied (thanks, ok, etc.), or navigates to a link provided by the agent
- Escalation rate: the customer goes to email the escalated ticket 
- Goal at first is resolution rate of 50% and escalation rate of 25% and have 25% fall through the cracks ie. the user leaves without expressing that the issue has been resolved 
- Average conversation length is under 1 minute (sub 45 seconds for voice)
- Agent response time is appropriate (check the performance metrics above)

# Tech Stack
Language is Python, LLM provider is perhaps just one provider such as OpenAI using both text and voice models from them. Web framework is likely FastAPI. Deployment is unknown, but normally statically handled by UChicago IT (so will need some way to tack onto the deployment). The agent will be deployed separately on a cloud server and embedded into the  static site.

# Risks 
- Deployment with the UChicago IT system of just a static HTML (and integration wth current website)
- How to safely protect against adversaries, abuse, and jailbreak attempts
- Dependencies on voice/model providers and data/infrastructure providers 
- Where to host/store the data and how to manage the deployment (when done by third party IT) 
- How to include both voice and text as options (voice is not just STT) 
- Knowledge base maintenance: the code for the agent shouldn't have to be updated on the regular, but the agent should be able to pull info from a refreshed knowledge base on github pushes (ie. someone who can use github and make text updates but not edit the agent itself) 
