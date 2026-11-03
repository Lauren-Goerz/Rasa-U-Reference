<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Add searchable documents to your Rasa Agent.


`EnterpriseSearchPolicy` indexes every `.txt` file in `docs/` when you train. Create the folder and add two files: one covering banking products, one covering policies.  
Write related facts together in one paragraph under a single heading. FAISS retrieves chunks, so information split across multiple short sections may only return part of the answer. A single paragraph per topic gives the agent everything it needs in one retrieval.
 
<p style="font-family:'IBM Plex Sans',sans-serif; font-size:14px; font-weight:500; margin:0 0 12px;"></p>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; font-family:'IBM Plex Sans',sans-serif; font-size:13px;">
  <div style="border:1px solid #f5c6c6; border-radius:6px; overflow:hidden; background:#fff8f8;">
    <div style="background:#fdecea; padding:8px 12px; border-bottom:1px solid #f5c6c6;">
      <span style="font-weight:500; color:#ce3381;">&#10007; Avoid — split headings</span>
    </div>
    <div style="padding:12px;">
      <div style="background:#fff; border:1px solid #eee; border-radius:4px; padding:10px; font-size:12px; line-height:1.7;">
        <div style="font-weight:600; font-size:13px; margin-bottom:2px;">Checking fees</div>
        <div style="color:#444; margin-bottom:10px;">It is \$5 per month, below \$500 dollars.</div>
        <div style="font-weight:600; font-size:13px; margin-bottom:2px;">Savings fees</div>
        <div style="color:#444;">No monthly fee.</div>
      </div>
      <p style="color:#666; margin:10px 0 0; line-height:1.5;">FAISS retrieves one chunk at a time. Split sections may return only half the answer, causing the agent to loop.</p>
    </div>
  </div>
  <div style="border:1px solid #c4baf9; border-radius:6px; overflow:hidden; background:#f5f3ff;">
    <div style="background:#ebe8fe; padding:8px 12px; border-bottom:1px solid #c4baf9;">
      <span style="font-weight:500; color:#5a17ee;">&#10003; Better — one paragraph</span>
    </div>
    <div style="padding:12px;">
      <div style="background:#fff; border:1px solid #eee; border-radius:4px; padding:10px; font-size:12px; line-height:1.7;">
        <div style="font-weight:600; font-size:13px; margin-bottom:2px;">Account fees</div>
        <div style="color:#444;">Checking accounts have no monthly fee when you maintain a balance of \$500 or more. A \$5 monthly fee applies below that threshold. Savings accounts have no monthly fee.</div>
      </div>
      <p style="color:#666; margin:10px 0 0; line-height:1.5;">Related facts in one paragraph = one retrieval = complete answer.</p>
    </div>
  </div>
</div>
<hr style="margin: 20px 0; border: none; border-top: 1px solid #dfe8ff;">
If you see the agent repeating the same answer on follow-up messages, the document structure is usually the cause.
 
## Add your Documents
#### banking_products.txt
 
Create `chapter5/docs/banking_products.txt`:
 
```txt
Account Fees
Checking accounts have no monthly fee when you maintain a balance of $500 or more. A $5 monthly fee applies below that threshold. Savings accounts have no monthly fee and no minimum balance requirement.
 
Account Features
Checking accounts include a debit card at no extra cost. The savings account earns 2.5% APY, calculated daily and credited monthly. Replacement debit cards cost $5. International debit card transactions carry a 1.5% fee per transaction.
 
Credit Cards
Three credit card tiers are available. The Standard card charges 18.99% APR. The Gold card charges 16.99% APR. The Platinum card charges 14.99% APR and requires a credit score of 750 or above.
 
Loyalty Cards
Loyalty cards earn 1 point per dollar spent at partner merchants. Points can be redeemed for statement credits at a rate of 100 points per $1.
```
 
#### banking_policies.txt
 
Create `chapter5/docs/banking_policies.txt`:
 
```txt
Transfer Limits and Fees
Standard accounts can transfer up to $5,000 per day. Business accounts have a $25,000 daily limit. International wire transfers have a $10,000 daily limit regardless of account type. Transfers between accounts at this bank are free. Transfers to external bank accounts cost $3 per transaction. International wire transfers cost $25.
 
ATM Access
The bank operates 2,000 fee-free ATMs nationwide. Out-of-network ATM withdrawals cost $2.50 per transaction.
 
Account Security
Two-factor authentication is required for any transfer over $500. Accounts are locked after five consecutive failed login attempts. Suspicious transactions are automatically flagged and may require phone verification before processing.
 
Opening an Account
New accounts can be opened online or in a branch. A government-issued ID and Social Security number are required. There is no minimum opening deposit for checking accounts. Savings accounts require a $100 opening deposit.
```


 
{Check It!|assessment}(code-output-compare-18512700)



---


