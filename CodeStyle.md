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
    return $arg1 * $arg2;
}
```

If code profiling and benchmarking shows that array args would be beneficial then a new sub is added with the same name but _aa appended.  There are some long-standing exceptions to this rule, for example ```get_param```, but new code should follow this pattern.

The number of args for such _aa subs should be three or fewer (excluding the object itself).


```perl 
sub some_sub_aa {
    my ($self, $arg1, $arg2) = @_;
    #  do stuff
    return $arg1 * $arg2
}
```

The ```$_[$i]``` method of accessing sub arguments will only be used where profiling demonstrates it is of benefit, and in short subs of a few lines.  In these cases comments should be added to explain why. 

```perl 
sub some_sub_aa {
    #  very hot path, avoid generation of lexical vars
    #my ($self, $arg1, $arg2) = @_;
    #  do stuff
    return $_[1] * $_[2];
}
```

## Sub return values ##

If there are many items to return from a sub then use a hash, ideally accounting for context:

E.g., instead of:
```perl
return ($res1, $res2, \%res3);
```

use:
```perl
my %results = (
    key1 => $res1,
    key2 => $res2,
    key3 => \%res3,
);
return wantarray ? %results : \%results;
```

Return refs to structures in scalar context will be faster in hot paths, as there is less for the caller to process.  

## Align and tabulate where reasonable ##

```perl
my $var1 = 'some value';
my $var_extra = 'some other value';
my %hash = (
    key => 5,
    longish => 10,
    really_long_key_that_seems_not_to_end => 1000,
);
```

can be clearer as:

```perl
my $var1      = 'some value';
my $var_extra = 'some other value';
my %hash = (
    key     =>  5,
    longish => 10,
    really_long_key_that_seems_not_to_end => 1000,
);
```

There are no hard rules for where the alignments should be, so use personal judgment as to what is visually clearer.  

