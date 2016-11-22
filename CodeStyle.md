An evolving list of code styles to use in Biodiverse development.

For the most part we follow the guides in Perl Best Practices.

## PBP related stuff ##
1.  Indentation should use units of four spaces, not tabs.  xt\07-notabs.t can be used to check for this. 
2.  Avoid camelCase names.  Use snake_case instead.
3.  Double sigil dereferencing is permitted (this differs from PBP).
4.  Postfix conditionals should be used for program control (```croak $msg if...```, ```return $x if...```).

## Sub arguments ##
Subs should use keyword/value (hash based) arguments, unless speed known to be an issue.  This makes extending function arguments much easier.  If code prfiling and benchmarking shows that array args would be beneficial then a new sub is added with the same name but _aa appended.  

There are some exceptions to this rule, for example get_param, but new code should follow this pattern.

