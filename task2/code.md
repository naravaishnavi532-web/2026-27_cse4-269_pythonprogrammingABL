# Progressive Electricity Billing System

## 1. Problem Statement

Design a Python program to calculate household electricity bills using a progressive billing system. The program should calculate charges based on multiple electricity consumption slabs, fixed charges, additional surcharges, and applicable rebates. It should accept electricity consumption details for several months, calculate the total bill for each month, compare monthly bills, and identify unusual increases in electricity charges.

Billing rules used in this program (sample values):

| Electricity consumption  | Rate per unit |
| ------------------------ | ------------- |
| First 100 units          | ₹2            |
| Next 100 units (101–200) | ₹3            |
| Above 200 units          | ₹5            |

Additional rules:

- Fixed charge: ₹50 per month.
- Surcharge: 5% of energy charges.
- Rebate: ₹20 if energy consumption is below 100 units.
- An increase of more than 30% compared with the previous month's bill is considered unusual.

## 2. Algorithm

1. Start.
2. Input the number of months.
3. For each month, input electricity consumption in units.
4. Calculate energy charges using progressive slabs:
   - First 100 units at ₹2 per unit.
   - Next 100 units at ₹3 per unit.
   - Remaining units at ₹5 per unit.
5. Add the fixed charge of ₹50.
6. Calculate a 5% surcharge on energy charges.
7. If consumption is below 100 units, subtract a rebate of ₹20.
8. Calculate the final electricity bill.
9. Store the monthly bill.
10. Compare each month's bill with the previous month's bill.
11. If the bill increases by more than 30%, identify it as an unusual increase.
12. Display monthly bills and unusual increases.
13. Stop.

## 3. Flowchart

\#chatgpt-mermaid-\_r_ja\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_ja\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_ja\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_ja\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_ja\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ja\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_ja\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_ja\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_ja\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_ja\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_ja\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_ja\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_ja\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_ja\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_ja\_ p{margin:0;}#chatgpt-mermaid-\_r_ja\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ja\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ja\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ja\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_ja\_ .label text,#chatgpt-mermaid-\_r_ja\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ja\_ .node rect,#chatgpt-mermaid-\_r_ja\_ .node circle,#chatgpt-mermaid-\_r_ja\_ .node ellipse,#chatgpt-mermaid-\_r_ja\_ .node polygon,#chatgpt-mermaid-\_r_ja\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_ja\_ .rough-node .label text,#chatgpt-mermaid-\_r_ja\_ .node .label text,#chatgpt-mermaid-\_r_ja\_ .image-shape .label,#chatgpt-mermaid-\_r_ja\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_ja\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_ja\_ .rough-node .label,#chatgpt-mermaid-\_r_ja\_ .node .label,#chatgpt-mermaid-\_r_ja\_ .image-shape .label,#chatgpt-mermaid-\_r_ja\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_ja\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_ja\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_ja\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_ja\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_ja\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_ja\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_ja\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_ja\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_ja\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_ja\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_ja\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ja\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ja\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_ja\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ja\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_ja\_ .icon-shape,#chatgpt-mermaid-\_r_ja\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_ja\_ .icon-shape p,#chatgpt-mermaid-\_r_ja\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_ja\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_ja\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_ja\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_ja\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_ja\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_ja\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_ja\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_ja\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_ja\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ja\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_ja\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_ja\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_ja\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ja\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_ja\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_ja\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ja\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_ja\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_ja\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ja\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_ja\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ja\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_ja\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_ja\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_ja\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_ja\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_ja\_ .node rect,#chatgpt-mermaid-\_r_ja\_ .node circle,#chatgpt-mermaid-\_r_ja\_ .node ellipse,#chatgpt-mermaid-\_r_ja\_ .node polygon,#chatgpt-mermaid-\_r_ja\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_ja\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_ja\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_ja\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_ja\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_ja\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput number of monthsSet month = 1month <= number of months?Input electricity unitsUnits <= 100?Energy charge = units \* 2Units <= 200?Energy charge = 200 +remaining units \* 3Energy charge = 500 +remaining units \* 5Add fixed charge and 5%surchargeUnits < 100?Subtract rebate of 20Calculate final billStore monthly billIs this the first month?Compare with previous billSkip comparisonIncrease greater than 30%?Identify unusual increaseNo unusual increaseDisplay monthly billIncrement monthDisplay all bills and unusualincreasesStopYesYesNoYesNoYesNoNoYesYesNoNo

## 4. Python Source Code

```
bills = []n = int(input("Enter number of months: "))for i in range(n):    print("\nMonth", i + 1)    units = float(input("Enter electricity units consumed: "))    if units <= 100:        energy = units * 2    elif units <= 200:        energy = 200 + (units - 100) * 3    else:        energy = 500 + (units - 200) * 5    fixed = 50    surcharge = energy * 0.05    rebate = 20 if units < 100 else 0    total = energy + fixed + surcharge - rebate    bills.append(total)    print("Energy Charge:", energy)    print("Fixed Charge:", fixed)    print("Surcharge:", surcharge)    print("Rebate:", rebate)    print("Total Bill: Rs.", round(total, 2))print("\nMonthly Bill Comparison")for i in range(n):    print("Month", i + 1, "Bill: Rs.", round(bills[i], 2))    if i > 0:        increase = ((bills[i] - bills[i-1]) / bills[i-1]) * 100
```

## 5. Sample Input

```
Enter number of months: 3

Month 1
Enter electricity units consumed: 80

Month 2
Enter electricity units consumed: 120

Month 3
Enter electricity units consumed: 250
```

## 6. Sample Output

```
Month 1
Energy Charge: 160.0
Fixed Charge: 50
Surcharge: 8.0
Rebate: 20
Total Bill: Rs. 198.0

Month 2
Energy Charge: 260.0
Fixed Charge: 50
Surcharge: 13.0
Rebate: 0
Total Bill: Rs. 323.0

Month 3
Energy Charge: 750.0
Fixed Charge: 50
Surcharge: 37.5
Rebate: 0
Total Bill: Rs. 837.5

Monthly Bill Comparison

Month 1 Bill: Rs. 198.0
Month 2 Bill: Rs. 323.0
Unusual Increase: 63.13 %
Month 3 Bill: Rs. 837.5
Unusual Increase: 159.29 %
```

## 7. Mermaid Flowchart Code

Copy this code into the [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to view or download your flowchart.

\#chatgpt-mermaid-\_r_k5\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_k5\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_k5\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_k5\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_k5\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_k5\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_k5\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_k5\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_k5\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_k5\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_k5\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_k5\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_k5\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_k5\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_k5\_ p{margin:0;}#chatgpt-mermaid-\_r_k5\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_k5\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_k5\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_k5\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_k5\_ .label text,#chatgpt-mermaid-\_r_k5\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_k5\_ .node rect,#chatgpt-mermaid-\_r_k5\_ .node circle,#chatgpt-mermaid-\_r_k5\_ .node ellipse,#chatgpt-mermaid-\_r_k5\_ .node polygon,#chatgpt-mermaid-\_r_k5\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_k5\_ .rough-node .label text,#chatgpt-mermaid-\_r_k5\_ .node .label text,#chatgpt-mermaid-\_r_k5\_ .image-shape .label,#chatgpt-mermaid-\_r_k5\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_k5\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_k5\_ .rough-node .label,#chatgpt-mermaid-\_r_k5\_ .node .label,#chatgpt-mermaid-\_r_k5\_ .image-shape .label,#chatgpt-mermaid-\_r_k5\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_k5\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_k5\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_k5\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_k5\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_k5\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_k5\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_k5\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_k5\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_k5\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_k5\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_k5\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_k5\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_k5\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_k5\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_k5\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_k5\_ .icon-shape,#chatgpt-mermaid-\_r_k5\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_k5\_ .icon-shape p,#chatgpt-mermaid-\_r_k5\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_k5\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_k5\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_k5\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_k5\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_k5\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_k5\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_k5\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_k5\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_k5\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_k5\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_k5\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_k5\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_k5\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_k5\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_k5\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_k5\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_k5\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_k5\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_k5\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_k5\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_k5\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_k5\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_k5\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_k5\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_k5\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_k5\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_k5\_ .node rect,#chatgpt-mermaid-\_r_k5\_ .node circle,#chatgpt-mermaid-\_r_k5\_ .node ellipse,#chatgpt-mermaid-\_r_k5\_ .node polygon,#chatgpt-mermaid-\_r_k5\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_k5\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_k5\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_k5\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_k5\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_k5\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput number of monthsSet month = 1month <= n?Input units consumedUnits <= 100?Energy = units \* 2Units <= 200?Energy = 200 + remaining \* 3Energy = 500 + remaining \* 5Calculate surcharge and fixedchargeUnits < 100?Subtract rebateCalculate total billStore billFirst month?Display billCompare with previous billIncrease 30%?Display unusual increaseDisplay normal changeIncrement monthDisplay monthly billcomparisonStopYesYesNoYesNoYesNoYesNoYesNoNo

## 8. Result

The Progressive Electricity Billing System successfully calculates monthly electricity bills using multiple consumption slabs, fixed charges, surcharges, and rebates. It compares bills across several months and identifies unusual increases in electricity charges.

Note: All billing rates and thresholds are assumed values for this program and can be modified according to actual electricity tariff rules.
