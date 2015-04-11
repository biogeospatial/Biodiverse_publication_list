use strict;
use warnings;
use 5.010;

my $re_bad_anchor = qr /#\w+_\w+\.md/;
my $re_issues     = qr {https://code.google.com/p/biodiverse/issues/detail\?id=#?};

my @files = glob '*.md';

foreach my $file (@files) {
    open (my $fh, '<', $file) or die "Cannot open $file";
    say $file;
    
    my $full_file;
    my $changed;
    while (my $line = <$fh>) {
        if (my @matches = $line =~ /($re_bad_anchor)/g) {
            foreach my $match (@matches) {
                my $repl = lc $match;
                $repl =~ s/_/-/g;
                $repl =~ s/\.md$//;
                say "$file $match $repl";
                $line =~ s/$match/$repl/;
                $changed ++;
            }
        }
        if ($line =~ /$re_issues\d/) {
            $line =~ s{$re_issues\d}{/shawnlaffan/biodiverse/issues/}g;
            $changed ++;
            say "$file has issues URL";
        }
        #if ($line =~ /\\_/) {
        #    $line =~ s/\\_/_/g;
        #    $changed ++;
        #}
        
        
        $full_file .= $line;
    }
    
    $fh->close;
    if ($changed) {
        open (my $ofh, '>', $file) or die "Cannot open $file";
        print {$ofh} $full_file;
        $ofh->close;
        #last;  #  DEBIG DEBUG
    }
    
}