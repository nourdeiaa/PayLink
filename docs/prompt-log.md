# PayLink -- AI Prompt Log

*Project:* PayLink -- Egyptian Bill-Payment and Digital-Wallet

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
