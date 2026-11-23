# PayLink – AI Prompt Log

*Project:* PayLink – Egyptian Bill Payment and Digital Wallet Backend  
*Date:* 23 November 2026  
*AI Tool Used:* ChatGPT — GPT-6

---

## Mariam – Requirements

### 1. User Stories and Acceptance Criteria

*Date:* 2026-11-23  
*Stage:* Requirements  
*Tool and Model:* ChatGPT — GPT-6

*Prompt:*

> Act as a business analyst. For PayLink, an Egyptian bill-payment and digital-wallet backend, create 28 user stories about registering customers, viewing wallet balances, topping up wallets, and paying bills. Use the format "As a [user], I want [goal], so that [benefit]." Give each story a Must, Should, or Could priority and write acceptance criteria in Given/When/Then format. Follow the project brief and do not invent business rules.

*Summary of AI Answer:*

Generated 28 user stories with priorities and Given/When/Then acceptance criteria.

*Verdict: ACCEPTED*

The generated stories were checked against the project brief and matched the stated requirements.

---

### 2. Requirements Edge Cases

*Date:* 2026-11-23  
*Stage:* Requirements  
*Tool and Model:* ChatGPT — GPT-6

*Prompt:*

> Act as a requirements reviewer. Review PayLink's requirements and identify 5 important edge cases involving duplicate payment requests, simultaneous wallet payments, biller timeouts, duplicate callbacks, and notification failures. Explain the expected behaviour for each case. Use only the project brief and label unspecified behaviour as a question for the team.

*Summary of AI Answer:*

Identified important edge cases and explained the expected system behaviour for each one.

*Verdict: FIXED*

Removed assumptions that were not supported by the project brief and discussed unclear cases with the team.


-------------------------------------------------------------------------------------------


## Aya – Design

### 3. Domain Class Diagram

*Date:* 2026-11-23  
*Stage:* Design  
*Tool and Model:* ChatGPT — GPT-6

*Prompt:*

> Act as a UML designer. Create a PlantUML domain class diagram for PayLink containing Customer, Wallet, LedgerEntry, Payment, Biller, Service, FeeRule, and Agent. Include important attributes, relationships, and multiplicities. Every wallet balance change must be represented by ledger entries. Provide the complete editable PlantUML source and explain each class.

*Summary of AI Answer:*

Generated a domain class diagram containing the main entities, attributes, and relationships.

*Verdict: FIXED*

Reviewed the relationships and ensured that the wallet and ledger classes correctly represented money movements.

---

### 4. Initial Payment Sequence Diagram

*Date:* 2026-11-23  
*Stage:* Design  
*Tool and Model:* ChatGPT — GPT-6

*Prompt:*

> Create a PlantUML sequence diagram for a customer paying a bill in PayLink. Include the customer, application, wallet, and biller. Show successful and failed payments.

*Summary of AI Answer:*

Generated a basic sequence diagram showing the main payment flow, but some important failure-handling details were missing.

*Verdict: REJECTED*

The first answer did not include all required payment outcomes and did not explain what happens to held funds.

---

### 5. Improved Payment Sequence Diagram

*Date:* 2026-11-23  
*Stage:* Design  
*Tool and Model:* ChatGPT — GPT-6

*Prompt:*

> Improve the previous PayLink payment sequence diagram. Include Customer, PayLink API, Payment Service, Fraud Check, Wallet/Ledger Service, Fee Service, Biller Adapter, External Biller, and Notification Service. Show fraud checks, fee calculation, holding funds before calling the biller, and three outcomes: success, refusal, and timeout after 10 seconds. Success must lead to Completed; refusal must lead to Failed and release the hold; timeout must lead to Unknown while funds remain held. Use PlantUML with alt/else blocks. Do not invent state transitions or automatically refund Unknown payments.

*Summary of AI Answer:*

Generated a more complete sequence diagram with the required participants and three biller outcomes.

*Verdict: FIXED*

The improved prompt produced a clearer diagram and included the held funds and Unknown state that were missing from the previous version.

---

## Aya – DevOps

### 6. Dockerfile for FastAPI

*Date:* 2026-11-23  
*Stage:* DevOps  
*Tool and Model:* ChatGPT — GPT-6

*Prompt:*

> Act as a DevOps engineer. Our PayLink team selected Python FastAPI. Create a simple Dockerfile for an empty FastAPI application. Use Python 3, install dependencies from requirements.txt, start the application using Uvicorn, and expose port 8000. Do not include a database in the Dockerfile. Explain every instruction and provide the commands to build and run the container.

*Summary of AI Answer:*

Generated a basic Dockerfile and explained how to build and run the FastAPI container.

*Verdict: ACCEPTED*

Checked that the Dockerfile matched the team's framework, application entry point, and port configuration.