# PayLink -- AI Prompt Log

*Project:* PayLink -- Egyptian Bill-Payment and Digital-Wallet


| Date | Author | Stage | Tool and model | Prompt | Summary of answer (2 lines) | Verdict (accepted, fixed, rejected) and why |
|---|---|---|---|---|---|---|
| 2026-11-23 | Mariam | Requirements | ChatGPT (GPT-6) | **ROLE:** Act as a business analyst.<br><br>**CONTEXT:** PayLink is an Egyptian bill-payment and digital-wallet backend.<br><br>**TASK:** Create 28 user stories for customer registration, wallet viewing, top-ups and bill payments. Use "As a \[user\], I want \[goal\], so that \[benefit\]."<br><br>**CONSTRAINTS:** Assign Must, Should or Could priority. Follow the project brief and do not invent business rules.<br><br>**OUTPUT:** User stories with Given/When/Then acceptance criteria. | Generated 28 user stories with priorities and acceptance criteria. The stories were checked against the project brief. | **ACCEPTED.** The stories matched the requirements stated in the project brief. |
| 2026-11-23 | Mariam | Requirements | ChatGPT (GPT-6) | **ROLE:** Act as a requirements reviewer.<br><br>**CONTEXT:** PayLink is a bill-payment and wallet backend.<br><br>**TASK:** Identify edge cases involving duplicate payment requests, simultaneous wallet payments, biller timeouts, duplicate callbacks and notification failures.<br><br>**CONSTRAINTS:** Use only the project brief. Mark unspecified behavior as a question for the team.<br><br>**OUTPUT:** Explain the expected behavior for each case. | Identified important payment and notification edge cases. The initial answer included assumptions that needed to be checked. | **FIXED.** Removed unsupported assumptions and discussed unclear behavior with the team. The revised prompt was prepared but not re-run. |
| 2026-11-23 | Aya | Design | Claude Sonnet 5.5 | **ROLE:** Act as a UML designer.<br><br>**CONTEXT:** PayLink wallet and bill-payment backend.<br><br>**TASK:** Create or correct a PlantUML domain class diagram containing Customer, Wallet, LedgerEntry, Payment, Biller, Service, FeeRule and Agent. Include attributes, relationships and multiplicities.<br><br>**CONSTRAINTS:** Follow the assignment's payment lifecycle. Derive wallet balances from ledger entries. Include the required fee and ledger-entry types. Do not add unsupported classes.<br><br>**OUTPUT:** Complete editable PlantUML source and a list of corrections. | The first diagram contained incorrect payment statuses and stored wallet balances. The improved diagram corrected these issues and was checked against the ER diagram and requirements. | **FIXED, THEN ACCEPTED.** The first answer used incorrect payment states and stored balances. The improved prompt identified the defects and supplied the relevant assignment rules. |
| 2026-11-23 | Aya | Design | Claude Sonnet 5.5 | **ROLE:** Act as a software architect and UML designer.<br><br>**CONTEXT:** PayLink bill-payment backend and its payment lifecycle.<br><br>**TASK:** Create a sequence diagram for paying a bill. Include the customer, PayLink modules, biller, fraud checks, fee calculation, wallet hold, idempotency and notifications.<br><br>**CONSTRAINTS:** Show success, biller refusal and a 10-second timeout. A timeout becomes Unknown and keeps funds held. Do not automatically refund Unknown payments. Apply agent commission only to completed agent payments.<br><br>**OUTPUT:** Complete valid PlantUML sequence diagram and a mapping to the payment steps in the brief. | The first diagrams omitted important payment handling and used incorrect states. The final improved diagram included the required flow, outcomes and payment lifecycle. | **REJECTED, THEN ACCEPTED.** Earlier versions omitted key steps or used incorrect states. The final prompt listed the missing behavior and exact lifecycle rules. |
| 2026-11-25 | Nour | Design | Claude Sonnet 5.5 | **ROLE:** Act as a UML designer.<br><br>**CONTEXT:** PayLink's payment lifecycle and failed-payment refund requirements.<br><br>**TASK:** Create a sequence diagram for refunding a failed payment, covering biller refusal and an Unknown payment later confirmed as not received.<br><br>**CONSTRAINTS:** Release the hold, create a ledger entry, set the status to Refunded and notify the customer. Never refund Unknown before confirmation. Do not refund Completed payments or invent states.<br><br>**OUTPUT:** One complete, valid PlantUML sequence diagram. | Corrected the refund flow to cover both failure paths. The diagram included hold release, ledger recording, Refunded status and notification. | **ACCEPTED.** The earlier committed diagram refunded a Completed payment and used unsupported states. The improved diagram followed the assignment lifecycle. |
| 2026-11-25 | Nour | Design | Claude Sonnet 5.5 | **ROLE:** Act as a UML designer.<br><br>**CONTEXT:** PayLink actors and functional requirements FR-1 to FR-28.<br><br>**TASK:** Review and correct the use-case diagram for Customer, Agent, Admin, Support Employee, Biller and Notification Provider.<br><br>**CONSTRAINTS:** Remove duplicate use cases. Cover required functions, including agent top-up, Unknown payment re-query, notification retry, reconciliation and audit logging. Use `<<include>>` for mandatory behavior and `<<extend>>` for optional or exceptional behavior. Map every use case to an FR.<br><br>**OUTPUT:** Complete valid PlantUML source and a use-case-to-FR table. | Corrected duplicate and missing use cases and added requirement traceability. The final diagram was rendered and reviewed after fixing a reversed relationship. | **REJECTED.** The committed diagram omitted required use cases and contained a duplicate. The first improved draft also had a reversed relationship and required further correction after the diagram was rendered. |
| 2026-11-23 | Nour | DevOps | ChatGPT (GPT-6) | **ROLE:** Act as a DevOps engineer.<br><br>**CONTEXT:** PayLink uses Python FastAPI and GitHub Actions.<br><br>**TASK:** Create `.github/workflows/ci.yml` to run on every push, install dependencies, lint the code and execute automated tests.<br><br>**CONSTRAINTS:** Use the repository's actual structure and commands. Do not include deployment steps.<br><br>**OUTPUT:** Complete workflow file and a brief explanation of its steps. | Generated a CI workflow for dependency installation, linting and tests. Repository paths and test commands required adjustment. | **FIXED.** Updated paths and commands to match the actual repository. A more detailed revised prompt was prepared but not re-run. |

## Summary

| Student | Stage | Activities | Final Verdicts |
|---|---|---|---|
| Mariam | Requirements | User stories and edge cases | 1 Accepted, 1 Fixed |
| Aya | Design | Class diagram and payment sequence diagram | 1 Fixed then Accepted, 1 Rejected then Accepted |
| Nour | Design | Refund sequence diagram and use-case diagram | 1 Accepted, 1 Rejected |
| Nour | DevOps | GitHub Actions CI workflow | 1 Fixed |

*Total AI interactions:* 7

*Overall observation:* AI assistance was used across Requirements, Design, and DevOps. Generated outputs were reviewed against the project brief and actual implementation needs. Some outputs were accepted directly, while others required corrections or rejection when they did not fully satisfy the project requirements.
=======
  --------------------------------------------------------------------------------------------------------------------------
  Date         Author     Stage          Tool and   Prompt                       Summary of answer     Verdict (accepted,
                                         model                                                         fixed, rejected) and
                                                                                                       why
  ------------ ---------- -------------- ---------- ---------------------------- --------------------- ---------------------
  2026-11-23   Mariam     Requirements   ChatGPT    **ROLE:** Act as a business  Generated 28 user     **ACCEPTED.** The
                                         (GPT-6)    analyst. **CONTEXT:**        stories with          stories matched the
                                                    PayLink is an Egyptian       priorities and        requirements stated
                                                    bill-payment and             acceptance criteria.  in the project brief.
                                                    digital-wallet backend.      The stories were      
                                                    **TASK:** Create 28 user     checked against the   
                                                    stories for customer         project brief.        
                                                    registration, wallet                               
                                                    viewing, top-ups and bill                          
                                                    payments. Use "As a                                
                                                    \[user\], I want \[goal\],                         
                                                    so that \[benefit\]."                              
                                                    **CONSTRAINTS:** Assign                            
                                                    Must, Should or Could                              
                                                    priority. Follow the project                       
                                                    brief and do not invent                            
                                                    business rules. **OUTPUT:**                        
                                                    User stories with                                  
                                                    Given/When/Then acceptance                         
                                                    criteria.                                          

  2026-11-23   Mariam     Requirements   ChatGPT    **ROLE:** Act as a           Identified important  **FIXED.** Removed
                                         (GPT-6)    requirements reviewer.       payment and           unsupported
                                                    **CONTEXT:** PayLink is a    notification edge     assumptions and
                                                    bill-payment and wallet      cases. The initial    discussed unclear
                                                    backend. **TASK:** Identify  answer included       behavior with the
                                                    edge cases involving         assumptions that      team. The revised
                                                    duplicate payment requests,  needed to be checked. prompt was prepared
                                                    simultaneous wallet                                but not re-run.
                                                    payments, biller timeouts,                         
                                                    duplicate callbacks and                            
                                                    notification failures.                             
                                                    **CONSTRAINTS:** Use only                          
                                                    the project brief. Mark                            
                                                    unspecified behavior as a                          
                                                    question for the team.                             
                                                    **OUTPUT:** Explain the                            
                                                    expected behavior for each                         
                                                    case.                                              

  2026-11-23 / Aya                                  **ROLE:** Act as a UML       The first diagram     **FIXED,** THEN
                                                     designer. **CONTEXT:**       contained incorrect   **ACCEPTED.** The first
                                         Claude     PayLink wallet and           payment statuses and  answer used incorrect
                                         Sonnet 5.5 bill-payment backend.        stored wallet         payment states and
                                                    **TASK:** Create or correct  balances. The         stored balances. The
                                                    a PlantUML domain class      improved diagram      improved prompt
                                                    diagram containing Customer, corrected these       identified the
                                                    Wallet, LedgerEntry,         issues and was        defects and supplied
                                                    Payment, Biller, Service,    checked against the   the relevant
                                                    FeeRule and Agent. Include   ER diagram and        assignment rules.
                                                    attributes, relationships    requirements.         
                                                    and multiplicities.                                
                                                    **CONSTRAINTS:** Follow the                        
                                                    assignment's payment                               
                                                    lifecycle. Derive wallet                           
                                                    balances from ledger                               
                                                    entries. Include the                               
                                                    required fee and                                   
                                                    ledger-entry types. Do not                         
                                                    add unsupported classes.                           
                                                    **OUTPUT:** Complete                               
                                                    editable PlantUML source and                       
                                                    a list of corrections.                             

  2026-11-23 / Aya                                 **ROLE:** Act as a software   The first diagrams    **REJECTED,** THEN
                                                   architect and UML designer.  omitted important     **ACCEPTED.** Earlier
                                         Claude     **CONTEXT:** PayLink         payment handling and  versions omitted key
                                         Sonnet 5.5 bill-payment backend and its used incorrect        steps or used
                                                    payment lifecycle. **TASK:** states. The final     incorrect states. The
                                                    Create a sequence diagram    improved diagram      final prompt listed
                                                    for paying a bill. Include   included the required the missing behavior
                                                    the customer, PayLink        flow, outcomes and    and exact lifecycle
                                                    modules, biller, fraud       payment lifecycle.    rules.
                                                    checks, fee calculation,                           
                                                    wallet hold, idempotency and                       
                                                    notifications.                                     
                                                    **CONSTRAINTS:** Show                              
                                                    success, biller refusal and                        
                                                    a 10-second timeout. A                             
                                                    timeout becomes Unknown and                        
                                                    keeps funds held. Do not                           
                                                    automatically refund Unknown                       
                                                    payments. Apply agent                              
                                                    commission only to completed                       
                                                    agent payments. **OUTPUT:**                        
                                                    Complete valid PlantUML                            
                                                    sequence diagram and a                             
                                                    mapping to the payment steps                       
                                                    in the brief.                                      

  2026-11-25   Nour       Design         Claude     **ROLE:** Act as a UML       Corrected the refund  **ACCEPTED.** The
                                         Sonnet 5.5 designer. **CONTEXT:**       flow to cover both    earlier committed
                                                    PayLink's payment lifecycle  failure paths. The    diagram refunded a
                                                    and failed-payment refund    diagram included hold Completed payment and
                                                    requirements. **TASK:**      release, ledger       used unsupported
                                                    Create a sequence diagram    recording, Refunded   states. The improved
                                                    for refunding a failed       status and            diagram followed the
                                                    payment, covering biller     notification.         assignment lifecycle.
                                                    refusal and an Unknown                             
                                                    payment later confirmed as                         
                                                    not received.                                      
                                                    **CONSTRAINTS:** Release the                       
                                                    hold, create a ledger entry,                       
                                                    set the status to Refunded                         
                                                    and notify the customer.                           
                                                    Never refund Unknown before                        
                                                    confirmation. Do not refund                        
                                                    Completed payments or invent                       
                                                    states. **OUTPUT:** One                            
                                                    complete, valid PlantUML                           
                                                    sequence diagram.                                  

  2026-11-25   Nour       Design         Claude     **ROLE:** Act as a UML       Corrected duplicate   **REJECTED.** The
                                         Sonnet 5.5 designer. **CONTEXT:**       and missing use cases committed diagram
                                                    PayLink actors and           and added requirement omitted required use
                                                    functional requirements FR-1 traceability. The     cases and contained a
                                                    to FR-28. **TASK:** Review   final diagram was     duplicate. The first
                                                    and correct the use-case     rendered and reviewed improved draft also
                                                    diagram for Customer, Agent, after fixing a        had a reversed
                                                    Admin, Support Employee,     reversed              relationship and
                                                    Biller and Notification      relationship.         required further
                                                    Provider. **CONSTRAINTS:**                         correction after the
                                                    Remove duplicate use cases.                        diagram was rendered.
                                                    Cover required functions,                          
                                                    including agent top-up,                            
                                                    Unknown payment re-query,                          
                                                    notification retry,                                
                                                    reconciliation and audit                           
                                                    logging. Use `<<include>>`                         
                                                    for mandatory behavior and                         
                                                    `<<extend>>` for optional or                       
                                                    exceptional behavior. Map                          
                                                    every use case to an FR.                           
                                                    **OUTPUT:** Complete valid                         
                                                    PlantUML source and a                              
                                                    use-case-to-FR table.                              


  2026-11-23   Nour       DevOps         ChatGPT    **ROLE:** Act as a DevOps    Generated a CI        **FIXED.** Updated
                                         (GPT-6)    engineer. **CONTEXT:**       workflow for          paths and commands to
                                                    PayLink uses Python FastAPI  dependency            match the actual
                                                    and GitHub Actions.          installation, linting repository. A more
                                                    **TASK:** Create             and tests. Repository detailed revised
                                                    `.github/workflows/ci.yml`   paths and test        prompt was prepared
                                                    to run on every push,        commands required     but not re-run.
                                                    install dependencies, lint   adjustment.           
                                                    the code and execute                               
                                                    automated tests.                                   
                                                    **CONSTRAINTS:** Use the                           
                                                    repository's actual                                
                                                    structure and commands. Do                         
                                                    not include deployment                             
                                                    steps. **OUTPUT:** Complete                        
                                                    workflow file and a brief                          
                                                    explanation of its steps.                          
  --------------------------------------------------------------------------------------------------------------------------

