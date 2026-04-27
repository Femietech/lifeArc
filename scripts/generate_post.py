prompt = """
Act as an Institutional FX Terminal. Generate 5 signal cards.
For EACH card, include:
1. 'Confidence Score' (e.g. 92%).
2. 'Risk/Reward Ratio' (e.g. 1:3).
3. 'Market Sentiment' (e.g. ULTRA BULLISH).
4. 'Architect's View' (A technical explanation of the 'structure' of the trade).

Use this sleek HTML structure for each card:
<div class="md:col-span-4 bento-card glass rounded-[2rem] p-8 flex flex-col justify-between">
    <div>
        <div class="flex justify-between items-start mb-6">
            <h3 class="text-2xl font-black font-heading text-white">PAIR_NAME</h3>
            <span class="text-[10px] font-black bg-cyan-400 text-black px-2 py-1 rounded">SENTIMENT</span>
        </div>
        <div class="grid grid-cols-2 gap-4 mb-8">
            <div class="bg-white/5 p-4 rounded-2xl"><div class="text-[8px] text-slate-500 font-bold uppercase mb-1">Entry</div><div class="mono text-sm">VALUE</div></div>
            <div class="bg-white/5 p-4 rounded-2xl"><div class="text-[8px] text-slate-500 font-bold uppercase mb-1">Target</div><div class="mono text-sm text-cyan-400">VALUE</div></div>
        </div>
    </div>
    <div class="pt-6 border-t border-white/5">
        <div class="flex justify-between text-[10px] font-black text-slate-500 mb-2">
            <span>CONFIDENCE</span>
            <span>R:R</span>
        </div>
        <div class="flex justify-between text-xs font-bold text-white uppercase">
            <span>SCORE%</span>
            <span>RATIO</span>
        </div>
    </div>
</div>
"""
