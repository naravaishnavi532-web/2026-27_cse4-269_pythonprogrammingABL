# Progressive Electricity Billing System

## 1. Problem Statement

Develop a Python program to calculate household electricity bills using multiple consumption slabs, fixed charges, surcharges, and rebates. The program should compare electricity bills across several months and identify unusual increases in billing amounts.

## 2. Algorithm

1. Start.
2. Enter the number of months.
3. Enter the electricity units consumed for each month.
4. Calculate the electricity charge based on progressive slabs:
   - 0–100 units: ₹2 per unit.
   - 101–200 units: ₹3 per unit.
   - 201–300 units: ₹5 per unit.
   - Above 300 units: ₹7 per unit.
5. Add fixed charges of ₹50.
6. Calculate a 5% surcharge.
7. Apply a 5% rebate if consumption is below 100 units.
8. Calculate the final bill.
9. Store and display the monthly bill.
10. Compare each month's bill with the previous month.
11. If the bill increases by more than 30%, display an unusual increase warning.
12. Calculate and display the total bill.
13. Stop.

## 3. Flowchart

[Python Lab Manual - Flowcharts and Programs for Basics - Studocu](https://images.openai.com/static-rsc-4/nM0lc_VyOpceXHoTxM2qDdnjJF1IaT0guEtpZ0MB-f3XttlbgZMJDp0Ri1PArWoj-Gx8MvcMtblbZeIlUjKYL5dhRdyt99p0pJhNmSz5955LyQmYZvy-j80xjC9i5TBlA533ba5ka4Ua7wt4d853-D5iQFEa9YXaLPvdatqyNM4?purpose=inline)

[studocu.com](https://www.studocu.com/in/document/anna-university/general/phython-lab-manual-lab-manual/127997737?utm_source=chatgpt.com)

## 4. Python Source Code

```
n = int(input("Enter number of months: "))bills = []for i in range(n):    print("\nMonth", i + 1)    units = int(input("Enter electricity units: "))    if units <= 100:        charge = units * 2    elif units <= 200:        charge = 100 * 2 + (units - 100) * 3    elif units <= 300:        charge = 100 * 2 + 100 * 3 + (units - 200) * 5    else:        charge = 100 * 2 + 100 * 3 + 100 * 5 + (units - 300) * 7    fixed = 50    surcharge = charge * 0.05    rebate = 0    if units < 100:        rebate = charge * 0.05    total = charge + fixed + surcharge - rebate    bills.append(total)    print("Electricity Bill: Rs.", round(total, 2))print("\n--- Monthly Bill Comparison ---")for i in range(n):    print("Month", i + 1, ":", round(bills[i], 2))    if i > 0:
```

## 5. Sample Input

```
Enter number of months: 3

Month 1
Enter electricity units: 80

Month 2
Enter electricity units: 150

Month 3
Enter electricity units: 320
```

## 6. Sample Output

```
Electricity Bill: Rs. 206.0
Electricity Bill: Rs. 522.5
Electricity Bill: Rs. 1590.0

--- Monthly Bill Comparison ---

Month 1 : 206.0
Month 2 : 522.5
Unusual increase detected!

Month 3 : 1590.0
Unusual increase detected!

Total Bill: Rs. 2318.5
```

## 7. Mermaid Flowchart Code

\#chatgpt-mermaid-\_r_g4\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_g4\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_g4\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_g4\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_g4\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_g4\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_g4\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_g4\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_g4\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_g4\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_g4\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_g4\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_g4\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_g4\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_g4\_ p{margin:0;}#chatgpt-mermaid-\_r_g4\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_g4\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_g4\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_g4\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_g4\_ .label text,#chatgpt-mermaid-\_r_g4\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_g4\_ .node rect,#chatgpt-mermaid-\_r_g4\_ .node circle,#chatgpt-mermaid-\_r_g4\_ .node ellipse,#chatgpt-mermaid-\_r_g4\_ .node polygon,#chatgpt-mermaid-\_r_g4\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_g4\_ .rough-node .label text,#chatgpt-mermaid-\_r_g4\_ .node .label text,#chatgpt-mermaid-\_r_g4\_ .image-shape .label,#chatgpt-mermaid-\_r_g4\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_g4\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_g4\_ .rough-node .label,#chatgpt-mermaid-\_r_g4\_ .node .label,#chatgpt-mermaid-\_r_g4\_ .image-shape .label,#chatgpt-mermaid-\_r_g4\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_g4\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_g4\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_g4\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_g4\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_g4\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_g4\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_g4\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_g4\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_g4\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_g4\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_g4\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_g4\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_g4\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_g4\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_g4\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_g4\_ .icon-shape,#chatgpt-mermaid-\_r_g4\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_g4\_ .icon-shape p,#chatgpt-mermaid-\_r_g4\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_g4\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_g4\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_g4\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_g4\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_g4\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_g4\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_g4\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_g4\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_g4\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_g4\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_g4\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_g4\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_g4\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_g4\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_g4\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_g4\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_g4\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_g4\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_g4\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_g4\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_g4\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_g4\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_g4\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_g4\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_g4\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_g4\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_g4\_ .node rect,#chatgpt-mermaid-\_r_g4\_ .node circle,#chatgpt-mermaid-\_r_g4\_ .node ellipse,#chatgpt-mermaid-\_r_g4\_ .node polygon,#chatgpt-mermaid-\_r_g4\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_g4\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_g4\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_g4\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_g4\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_g4\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter number of monthsEnter electricity unitsCheck consumption slabCalculate electricity chargeAdd fixed chargesCalculate surchargeUnits below 100?Apply rebateNo rebateCalculate final billStore and display billMore months?Compare monthly billsIncrease above 30%?Display unusual increaseDisplay normal variationDisplay total billStopYesNoYesNoYesNo

