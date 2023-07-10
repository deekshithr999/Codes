<h2 align = "center"> Heap Notes </h2>
<p> 

<h3> 1. Estimating Number of Leaves in a heap </h3>
<blockquote>
With increase in each level, the #of nodes in that level will be 2*prev level <br>
<code>#( Nodes at curr level) = 2* (Nodes at prev level) </code><br>
total nodes = 1 + 2 + 4 + 8 +16 + ... <br>
 so  #(sum of all prev level nodes) = #(last_level nodes -1) <br>
 Therefore ``#(leaves) = #(total nodes)/2`` <br/>
 <strong><em>NOTE:** start the index from 1</em></strong> <br/>
 </blockquote>
</p>
<!-- <hr> -->
<p>
<h3>2. How is /2 for parent nodes working completely fine in the code </h3>
<blockquote>If your look closely, the divide by 2 works bcz for each parent there will be 2 childs, so 2 childs compensate for each parent and the poor root will be vanished because of its +1 contribution bcz +1/2 = 0 <br>
But the +1 comes into picture when there is 1 child only for the last node making it (+1 +1 =2) accountable
</blockquote>
</p>
 

