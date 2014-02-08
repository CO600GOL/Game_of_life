<%def name="rule_one()">
    <p>Any living cell with fewer than two living neighbours will die due to under-population.</p>
</%def>

<%def name="rule_two()">
    <p>Any living cell with two or three living neighbours will survive on into the next generation.</p>
</%def>

<%def name="rule_three()">
    <p>Any living cell with more than three living neighbours will die due to over-population.</p>
</%def>

<%def name="rule_four()">
   <p>Any dead cell with exactly three living neighbours will be born in the next generation.</p>
</%def>