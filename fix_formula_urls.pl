#  Fix formula URLs given GitHub changed their format at some point

use strict;
use warnings;
use 5.010;
use URI::Escape qw /uri_escape/;

my $re_text_in_brackets;  #  straight from Friedl, page 330.  Could be overkill, but works
$re_text_in_brackets = qr / (?> [^()]+ | \(  (??{ $re_text_in_brackets }) \) )* /xo; #/
#  poss alternative for perl 5.10 and later:  qr /(\\((?:[^()]++|(?-1))*+\\))/xo
#  from http://blogs.perl.org/users/jeffrey_kegler/2012/08/marpa-v-perl-regexes-a-rematch.html

my $re_text_in_square_brackets;  #  modified from Friedl, page 330.
$re_text_in_square_brackets = qr / (?> [^\[\]]+ | \[  (??{ $re_text_in_square_brackets }) \] )* /xo; #/

my $re_image_url = qr /! ($re_text_in_square_brackets) ($re_text_in_brackets)/x;

my $code_cogs_url = 'http://latex.codecogs.com/png.latex';

my @files = glob 'Indices.md';

foreach my $file (@files) {
    open (my $fh, '<', $file) or die "Cannot open $file";
    say $file;
    
    my $full_file;
    my $changed;
    while (my $line = <$fh>) {
        #pos ($line) = 0;
        if ($line =~ /!(?=\[)/) {
            my @matches = $line =~ /! \[ ($re_text_in_square_brackets) \] \( ($re_text_in_brackets) \) /xg;
            while (@matches) {
                my ($url, $eqn) = (shift @matches, shift @matches);
                #say "$url : $eqn";
                my $orig_eqn = $eqn;
                #  url is unchanged
                $eqn =~ s|$code_cogs_url\?||;
                $orig_eqn =~ s|$code_cogs_url\?||;
                $eqn =~ s/\\\\/\\/g;
                $eqn =~ s/^= /=/;
                $eqn = uri_escape ($eqn);
                $eqn =~ s/\(/\\\(/g;
                $eqn =~ s/\)/\\\)/g;
                $eqn =~ s/%5C%5C/%5C\\/g;
                $orig_eqn = quotemeta $orig_eqn;
                $line =~ s/\($code_cogs_url\?$orig_eqn\)/\($code_cogs_url\?$eqn\)/;
                $changed ++;
            }
        }
        
        $full_file .= $line;
    }
    
    $fh->close;
    if ($changed) {
        $file =~ s/\.md$/x\.md/;
        open (my $ofh, '>', $file) or die "Cannot open $file";
        print {$ofh} $full_file;
        $ofh->close;
        #last;  #  DEBIG DEBUG
    }
    
}