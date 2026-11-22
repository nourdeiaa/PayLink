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

FR-10 — Idempotency

As a customer, I want repeated payment requests with the same idempotency key to return the original result, so that I am not charged twice.

- Given a payment request with a new idempotency key, when the request is processed, then PayLink creates one payment.
- Given a payment request that has already been processed, when the same key is sent again, then PayLink returns the original payment result.
- Given the same key is sent multiple times, when the requests are processed, then only one charge is made.
------------------------------------

FR-11 — Payment lifecycle

As a system, I want every payment to follow the defined payment lifecycle, so that payment status changes remain correct.

- Given a payment is Initiated and fraud checks pass with sufficient funds, when processing continues, then it becomes FundsHeld.
- Given a payment is SentToBiller, when the biller confirms payment, then it becomes Completed.
- Given a payment is Completed, when another status change is attempted, then the system rejects the invalid transition.
------------------------------------

FR-12 — Hold funds before calling the biller

As a customer, I want the payment amount to be held before PayLink contacts the biller, so that my wallet cannot spend the same money twice.

- Given the customer has enough available balance, when payment processing starts, then the required amount is moved to held funds.
- Given the funds have been held, when PayLink sends the payment request, then the biller is contacted.
- Given the biller refuses the payment, when the failure is confirmed, then the held funds are released.
------------------------------------

FR-13 — Handle payment timeouts

As a customer, I want a timed-out payment to be marked Unknown, so that I am not refunded when the biller may have received my payment.

- Given a payment has been sent to a live biller, when no response arrives within 10 seconds, then its status becomes Unknown.
- Given a payment is Unknown, when the retry schedule is reached, then PayLink re-queries after 1, 5, and 15 minutes.
- Given the payment remains Unknown after three retries, when retrying stops, then it waits for reconciliation.
------------------------------------

FR-14 — TopUpNet callbacks

As a system, I want to receive asynchronous callbacks from TopUpNet and ignore duplicates, so that a mobile top-up is processed only once.

- Given a TopUpNet payment request, when TopUpNet accepts it, then PayLink waits for the final callback.
- Given a valid success callback, when PayLink receives it, then the payment is completed.
- Given the same callback arrives twice, when the second callback is received, then it is ignored and logged.
------------------------------------

FR-15 — Support at least three billers

As a customer, I want to pay through different billers, so that I can use PayLink for electricity, water, and mobile top-up payments.

- Given a customer wants to pay an electricity bill, when they select ElectroCo, then PayLink uses its REST JSON integration.
- Given a customer wants to pay a water bill, when they select AquaCo, then PayLink handles its SOAP-style XML integration.
- Given a customer wants a mobile top-up, when they select TopUpNet, then PayLink handles its asynchronous callback process.
------------------------------------

FR-16 — Calculate fees correctly

As a customer, I want PayLink to calculate the correct service fee, so that I know the total amount before paying.

- Given an electricity or water bill, when the fee is calculated, then the fee is 2.50 EGP.
- Given a mobile top-up, when the fee is calculated, then it is 1.5% of the amount with a minimum of 1 EGP.
- Given an internet bill, when the fee is calculated, then it is 2 EGP for amounts up to 200 EGP and 4 EGP above 200 EGP.
- Given a valid promotion is active for a chosen biller, when its fee is calculated, then the fee is zero.
------------------------------------

FR-17 — Agent pays on behalf of a customer

As an agent, I want to pay a bill on behalf of a customer, so that the customer can use PayLink without using the mobile app.

- Given an agent is authorized, when they submit a customer's bill payment, then PayLink processes it for that customer.
- Given the payment is completed, when the commission is calculated, then the agent earns 40% of the service fee.
- Given the payment fails, when the failure is confirmed, then the agent does not receive commission.
------------------------------------

FR-18 — Payment limits

As a customer, I want PayLink to check my payment limits, so that I cannot make payments above my allowed limit.

- Given a customer makes a payment below the single-payment minimum of 5 EGP, when the request is checked, then it is rejected with a clear reason.
- Given a payment is above the single-payment maximum of 10,000 EGP, when the request is checked, then it is rejected.
- Given a basic customer has reached the daily limit of 5,000 EGP, when they attempt another payment, then it is rejected.
- Given a verified customer has reached the daily limit of 30,000 EGP, when they attempt another payment, then it is rejected.
------------------------------------

FR-19 — Payment velocity rule (Should)

As a system, I want to block accounts that make too many payments in a short time so that suspicious activity is prevented.
- Given an account makes more than 5 payments within 60 seconds,
- When the sixth or later payment is attempted,
- Then the account is blocked for 10 minutes.
------------------------------------

FR-20 — Search payment (Must)

As a support employee, I want to search for a payment by its reference so that I can investigate its history.
- Given a support employee has permission to access payment records,
- When they search using a payment reference,
- Then the system displays the payment's full history.
------------------------------------

FR-21 — Block and unblock accounts (Should)

As a support employee, I want to block and unblock customer accounts so that I can manage suspicious or problematic accounts.
- Given a support employee is authorized,
- When they block or unblock an account,
- Then the system updates the account status and records the action.
------------------------------------

FR-22 — Notifications (Must)

As a customer, I want to receive SMS and push notifications when a payment succeeds or fails so that I know its result.
- Given a payment is completed or failed,
- When the payment status changes,
- Then the system sends an SMS and push notification to the customer.
------------------------------------

FR-23 — Notification retries (Should)

As a system, I want to retry failed notifications so that temporary provider failures do not prevent customers from receiving updates.
- Given an SMS or email notification fails,
- When the system retries delivery,
- Then it retries 3 times and marks the notification as undelivered if all attempts fail.
------------------------------------

FR-24 — Edit fees and limits (Should)

As an admin, I want to edit fee and limit values without redeploying the application so that business rules can be updated easily.
- Given an admin is authorized,
- When they update a fee or limit,
- Then the system saves the new configuration without requiring redeployment.
------------------------------------

FR-25 — Audit log (Must)

As a system administrator, I want every money movement and admin action recorded so that activities can be traced.
- Given a money movement or admin action occurs,
- When the action is performed,
- Then the system records it in an audit log.
------------------------------------

FR-26 — Reconciliation report (Should)

As a support employee, I want a daily reconciliation report so that I can identify differences between PayLink payments and biller settlement files.
- Given a settlement file is received,
- When the reconciliation process runs,
- Then the system compares the file with PayLink's payment records and produces a report of differences.
------------------------------------

FR-27 — Request refund (Could)

As a customer, I want to request a refund for a completed payment so that support can review my refund request.
- Given a customer has a completed payment,
- When they submit a refund request,
- Then the system records the request for support approval.
------------------------------------

FR-28 — Daily totals (Could)

As an admin, I want to view daily payment statistics so that I can monitor business performance.
- Given daily payment data is available,
- When the admin opens the daily totals report,
- Then the system displays payments, fees earned, commissions paid and failures per biller.
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

NFR-3 — Modifiability

- Requirement: Adding a new biller should require changes only to the Biller Integration module and configuration. Existing modules should not need modification.
- Measurement: Demonstrate adding a new mock biller without changing Payment Processing, Accounts and Wallet, or Fees and Commissions.
------------------------------------

NFR-4 — Testability

- Requirement: At least 70% line coverage must be achieved on domain logic.
- Measurement: The automated CI pipeline produces a coverage report showing at least 70% coverage for domain logic.
------------------------------------

NFR-5 — Resilience
- Requirement: An outage of one biller must not stop payments to other billers.
- Measurement: Test that payments to an available biller still work while another mock biller is unavailable.
------------------------------------

NFR-6 — Auditability
- Requirement: Every money movement must have an audit record containing who, when and why.
- Measurement: 100% of money movements have the required audit record.
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
------------------------------------


