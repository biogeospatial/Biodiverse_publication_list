An evolving list of code styles to use in Biodiverse development.

For the most part we follow the guides in Perl Best Practices.

## PBP related stuff ##
1.  Indentation should use units of four spaces, not tabs.  xt\07-notabs.t can be used to check for this. 
2.  Avoid camelCase names.  Use snake_case instead.
3.  Double sigil dereferencing is permitted (this differs from PBP).
4.  Postfix conditionals should be used for program control (```croak $msg if...```, ```return $x if...```).

## Sub arguments ##
Subs should use keyword/value (hash based) arguments, unless speed known to be an issue.  This makes extending function arguments much easier.  

```perl
sub some_sub {
    my ($self, %args) = @_;
    my $arg1 = $args{argname1};
    my $arg2 = $args{argname2};
    #  do stuff
}
```

If code profiling and benchmarking shows that array args would be beneficial then a new sub is added with the same name but _aa appended.  There are some long-standing exceptions to this rule, for example ```get_param```, but new code should follow this pattern.

The number of args for such _aa subs should be three or fewer (excluding the object itself).


```perl 
sub some_sub_aa {
    my ($self, $arg1, $arg2) = @_;
    #  do stuff
}
```

The ```$_[$i]``` method of accessing sub arguments will only be used where profiling demonstrates it is of benefit, and in short subs of a few lines.  In these cases comments should be added to explain why. 


