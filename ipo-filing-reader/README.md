# IPO filing reader: who gets a better price than you

![Prompt card](assets/prompt-card.png)

One prompt that makes Claude read an IPO filing (S-1 or S-1/A) like a skeptical buyer and list every deal where an insider, partner or early investor gets a better price, more shares or more control than you at the IPO price. Each finding comes with the exact sentence and the page number, so you can check it yourself.

## Run it

1. Find the company on [SEC EDGAR](https://www.sec.gov/edgar/search/) and open the newest S-1/A. The newest amendment is the one with the price range.
2. Save the filing as a PDF or HTML file (File → Save in your browser). SEC limits automated downloads, so saving it yourself is the easy route.
3. Open Claude with file upload on, attach the file and paste the [prompt](prompt.md).
4. Answer its 3 questions, check the plan for the 3 passes, then say go.

Big filings run to hundreds of pages. If the file is too large for one chat, split it by section (the capitalization table, convertible notes, related-person transactions, shares eligible for future sale, underwriting) and run the prompt on each part.

## Example: Anthropic, November 2026

Run on Anthropic's S-1/A (Amendment No. 2, filed Nov 10, 2026), one of the things it surfaces sits on pages 171–172: Amazon's 2023 and 2024 notes convert at $2.0928 and $5.0478 a share, capped at 12% of the company. Whatever can't convert at the IPO stays as rollover notes and converts at the end of every quarter after the listing, and Amazon can waive the cap.

![Anthropic S-1/A, pages 171–172](assets/anthropic-s1-amazon-notes.png)

The excerpt is the filing's own text, retyped for readability, with the key lines highlighted. Source: [Anthropic S-1/A on EDGAR](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm).

## Rules

- Every claim needs a quote and a page number. If Claude can't point to the sentence, treat the claim as unverified.
- Prices in a filing are often before a stock split. The prompt asks Claude to adjust them; check that it did.
- This reports what the filing says. It is not a reason to buy or sell anything, and nothing here is financial advice.
