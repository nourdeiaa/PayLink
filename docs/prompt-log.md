*USE CASE DIAGRAM:*

@startuml
left to right direction

actor Customer
actor Agent
actor Admin
actor "Support Employee" as Support
actor Biller

rectangle PayLink {
  usecase "Register Account" as UC1
  usecase "Upgrade Verification" as UC2
  usecase "View Wallet" as UC3
  usecase "Top Up Wallet" as UC4
  usecase "View Transaction History" as UC5
  usecase "View Billers and Services" as UC6
  usecase "Inquire About Bill" as UC7
  usecase "Pay Bill" as UC8
  usecase "Manage Billers" as UC9
  usecase "Search Payment" as UC10
}

Customer --> UC1
Customer --> UC2
Customer --> UC3
Customer --> UC4
Customer --> UC5
Customer --> UC6
Customer --> UC7
Customer --> UC8

Agent --> UC8
Admin --> UC9
Support --> UC10
Biller --> UC7
Biller --> UC8

@enduml

-------------------------

*STATE DIAGRAM:*
@startuml

[*] --> Initiated

Initiated --> FundsHeld : Fraud checks pass and funds available
Initiated --> Rejected : Fraud check fails or insufficient funds

FundsHeld --> SentToBiller : Request sent to biller

SentToBiller --> Completed : Biller confirms
SentToBiller --> Failed : Biller refuses
SentToBiller --> Unknown : Timeout

Unknown --> Completed : Later confirmation
Unknown --> Failed : Later refusal or reconciliation finds no payment

Failed --> Refunded : Hold released to wallet

Completed --> [*]
Rejected --> [*]
Refunded --> [*]

@enduml

-------------------------

*CLASS DIAGRAM*
@startuml
title PayLink Domain Class Diagram

class Customer {
  +id: int
  +name: string
  +phone: string
  +verificationLevel: string
}

class Wallet {
  +id: int
  +availableBalance: decimal
  +heldBalance: decimal
}

class LedgerEntry {
  +id: int
  +amount: decimal
  +entryType: string
  +createdAt: datetime
}

class Payment {
  +id: int
  +reference: string
  +amount: decimal
  +fee: decimal
  +status: string
  +idempotencyKey: string
}

class Biller {
  +id: int
  +name: string
  +protocol: string
}

class Service {
  +id: int
  +name: string
  +active: boolean
}

class FeeRule {
  +id: int
  +feeType: string
  +feeValue: decimal
}

class Agent {
  +id: int
  +name: string
}

class Commission {
  +id: int
  +amount: decimal
  +status: string
}

Customer "1" -- "1" Wallet : owns
Wallet "1" -- "*" LedgerEntry : records
Customer "1" -- "*" Payment : makes
Payment "*" -- "1" Biller : sent to
Biller "1" -- "*" Service : provides
Service "1" -- "*" FeeRule : uses
Payment "1" -- "0..1" Commission : generates
Agent "1" -- "*" Commission : earns
Agent "0..1" -- "*" Payment : assists with

@enduml

-------------------------

*SEQUENCE DIAGRAM-PAYBILL*

@startuml
title PayLink - Pay a Bill Sequence

actor Customer
participant "Mobile App" as App
participant "Payment Service" as Payment
participant "Fraud Check" as Fraud
participant "Wallet Service" as Wallet
participant "Fee Service" as Fee
participant "Biller Adapter" as Adapter
participant "Biller" as Biller
participant "Notification Service" as Notification

Customer -> App: Select bill and enter details
App -> Payment: Submit payment request
Payment -> Payment: Check idempotency key

Payment -> Fraud: Validate customer and limits
Fraud --> Payment: Validation result

alt Fraud check fails
    Payment --> App: Reject payment
else Fraud check passes
    Payment -> Fee: Calculate service fee
    Fee --> Payment: Return fee and total

    Payment -> Wallet: Hold required amount
    Wallet --> Payment: Hold successful

    Payment -> Adapter: Send payment request
    Adapter -> Biller: Submit bill payment

    alt Biller confirms payment
        Biller --> Adapter: Success
        Adapter --> Payment: Payment confirmed
        Payment -> Wallet: Finalize held funds
        Payment -> Notification: Send success SMS and push
        Payment --> App: Completed
    else Biller refuses payment
        Biller --> Adapter: Failure
        Adapter --> Payment: Payment failed
        Payment -> Wallet: Release held funds
        Payment -> Notification: Send failure SMS and push
        Payment --> App: Failed
    else Biller times out
        Adapter --> Payment: Timeout
        Payment -> Payment: Set status to Unknown
        Payment --> App: Payment is being processed
    end
end

@enduml

-------------------------

*REFUND SEQUENCE DIAGRAM*

@startuml
actor Customer
participant "Payment Processing" as Payment
participant "Biller Integration" as Biller
participant "Accounts and Wallet" as Wallet
participant "Ledger" as Ledger
participant "Notifications" as Notify

Customer -> Payment: Pay bill
Payment -> Wallet: Hold payment funds
Wallet --> Payment: Hold created

Payment -> Biller: Send payment request
Biller --> Payment: Payment refused

Payment -> Payment: Change status to Failed
Payment -> Wallet: Release held funds
Wallet -> Ledger: Record fund release
Ledger --> Wallet: Entry recorded

Payment -> Notify: Send failure notification
Notify --> Customer: SMS and push notification

@enduml

-------------------------

*DATABASE ERD*

@startuml

entity Customer {
  * customer_id : int <<PK>>
  --
  name : string
  verification_level : string
  account_status : string
}

entity Agent {
  * agent_id : int <<PK>>
  --
  name : string
}

entity Wallet {
  * wallet_id : int <<PK>>
  --
  customer_id : int <<FK>>
  available_balance : decimal
  held_balance : decimal
}

entity LedgerEntry {
  * entry_id : int <<PK>>
  --
  wallet_id : int <<FK>>
  amount : decimal
  entry_type : string
  created_at : datetime
}

entity Biller {
  * biller_id : int <<PK>>
  --
  name : string
  protocol : string
  status : string
}

entity Service {
  * service_id : int <<PK>>
  --
  biller_id : int <<FK>>
  name : string
  status : string
}

entity Payment {
  * payment_id : int <<PK>>
  --
  customer_id : int <<FK>>
  service_id : int <<FK>>
  agent_id : int <<FK>>
  amount : decimal
  fee : decimal
  status : string
  reference : string
}

entity Hold {
  * hold_id : int <<PK>>
  --
  payment_id : int <<FK>>
  wallet_id : int <<FK>>
  amount : decimal
  status : string
}

entity FeeRule {
  * fee_rule_id : int <<PK>>
  --
  service_id : int <<FK>>
  fee_type : string
  fee_value : decimal
}

entity Commission {
  * commission_id : int <<PK>>
  --
  payment_id : int <<FK>>
  agent_id : int <<FK>>
  amount : decimal
}

entity Notification {
  * notification_id : int <<PK>>
  --
  payment_id : int <<FK>>
  channel : string
  status : string
  retry_count : int
}

entity AuditLog {
  * audit_id : int <<PK>>
  --
  actor_id : int
  action : string
  reason : string
  created_at : datetime
}

entity RefundRequest {
  * refund_id : int <<PK>>
  --
  payment_id : int <<FK>>
  customer_id : int <<FK>>
  status : string
}

entity SettlementFile {
  * file_id : int <<PK>>
  --
  biller_id : int <<FK>>
  received_at : datetime
}

entity ReconciliationDifference {
  * difference_id : int <<PK>>
  --
  file_id : int <<FK>>
  payment_id : int <<FK>>
  description : string
}

Customer ||--|| Wallet
Customer ||--o{ Payment
Customer ||--o{ RefundRequest
Agent ||--o{ Payment
Agent ||--o{ Commission

Wallet ||--o{ LedgerEntry
Wallet ||--o{ Hold
Biller ||--o{ Service
Service ||--o{ Payment
Service ||--o{ FeeRule

Payment ||--o{ Hold
Payment ||--o{ Notification
Payment ||--o{ Commission
Payment ||--o{ RefundRequest

Biller ||--o{ SettlementFile
SettlementFile ||--o{ ReconciliationDifference
Payment ||--o{ ReconciliationDifference

@enduml