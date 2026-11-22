# PayLink Requirements

## 1. Problem Summary

PayLink is an Egyptian digital payment platform that allows customers to pay electricity, water, mobile and internet bills using money stored in a digital wallet. Customers can also pay through agents. The system must process payments correctly, manage wallet balances, communicate with billers, and handle failed or delayed transactions without charging customers incorrectly.

## 2. Stakeholders

| Stakeholder       | Responsibility                                     |
| ----------------- | -------------------------------------------------- |
| Customers         | Register, manage wallets and pay bills             |
| Agents            | Pay bills on behalf of customers                   |
| Administrators    | Manage billers, services and system settings       |
| Support employees | Investigate payments and help customers            |
| Billers           | Provide bills and receive payments                 |
| Management        | Monitor fees, commissions and business performance |
| Engineering team  | Build, test and maintain PayLink                   |

## 3. Functional Requirements

FR-1 — Customer registration (Must)
As a customer, I want to register an account so that I can use PayLink.

- Given a new customer has valid registration information,
- When they submit the registration,
- Then the system creates their account with basic verification level.
------------------------------------

FR-2 — Upgrade verification (Should)
As a customer, I want to upgrade my verification level so that I can have higher payment limits.

- Given a customer has a basic account,
- When their verification upgrade is approved,
- Then their account becomes verified and uses the verified payment limit.
------------------------------------

FR-3 — View wallet (Must)
As a customer, I want to view my wallet balance and transaction history so that I can track my money.

- Given a customer is logged in,
- When they open their wallet,
- Then the system displays available balance, held balance and transaction history.
------------------------------------

FR-4 — Top up wallet (Must)
As a customer, I want to add money to my wallet so that I can pay bills.

- Given a customer has a valid wallet,
- When they complete a simulated card top-up or agent cash top-up,
- Then the system records the added money.
------------------------------------

FR-5 — Ledger entries (Must)
As a system administrator, I want every balance change recorded in a ledger so that all money movements can be tracked.

- Given a wallet balance changes,
- When the transaction is recorded,
- Then the system creates a ledger entry and computes the balance from ledger entries.
------------------------------------

FR-6 — Manage billers (Must)
As an admin, I want to add, edit and disable billers and services so that the available services stay up to date.

- Given an admin is authorized,
- When they add, edit or disable a biller or service,
- Then the system saves the change.
------------------------------------

FR-7 — View billers (Must)
As a customer, I want to see available billers and their required input fields so that I know what information to enter.

- Given a customer opens the biller list,
- When the system displays available billers,
- Then it shows each biller's services and required input fields.
------------------------------------

FR-8 — Bill inquiry (Must)
As a customer, I want to inquire about my bill so that I can see the amount and fees before paying.

- Given a customer selects a biller and enters the required information,
- When they request a bill inquiry,
- Then the system displays the bill amount, service fee and total amount.
------------------------------------

FR-9 — Pay bill (Must)
As a customer, I want to pay a bill from my wallet so that I can complete the payment without visiting the biller's office.

- Given the customer has sufficient available wallet funds,
- When they confirm the bill payment,
- Then the system begins the payment process and follows the defined payment lifecycle.
------------------------------------


## 4. Non-Functional Requirements

NFR-1 — Correctness

- Requirement: The system must prevent double charges and negative wallet balances.
- Measurement: Zero double charges and zero negative balances in duplicate-request and concurrency tests.
------------------------------------

NFR-2 — Performance

- Requirement: The system must support 100 payments per second.
- Measurement: Sustain 100 payments per second for one minute against mock billers.
------------------------------------

## 5. Questions, Ambiguities and Decisions

| Question or ambiguity                                  | Decision
|------------------------------------------------------  | --------------- 
| What is the daily payment limit for basic accounts?    | 5,000 EGP 
| What is the daily payment limit for verified accounts? | 30,000 EGP 
| What is the minimum single payment?                    | 5 EGP 
| What is the maximum single payment?                    | 10,000 EGP 
| Should wallet balances be changed directly?            | No. Every money movement must create a ledger entry. 
| What balances should customers see?                    | Available balance and held balance. 
| What happens when a bill inquiry is made?              | Display bill amount, fee and total before payment.
|
