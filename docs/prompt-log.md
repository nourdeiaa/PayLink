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