#!/usr/bin/perl

open(my $fin, '<', 'elements.dat');
my $data;
my $len = -1;
my $count = 0;
while (<$fin>) {
    @vars = split " ";
    $len = scalar(@vars) if ($len < 0);
    for (my $m = 0; $m < scalar(@vars); $m++) {
        $data->[$count][$m] = $vars[$m];      
    }
    $count++;
    last if (scalar(@vars) == 0);
}

for ($m = 0; $m < $len; $m++) {
    $var = lc $data->[0][$m];
    if ($m == 0) {
        print "$var = [ 0";
    } elsif (($m==1) || ($m ==2) || ($m == 8) || ($m==15)) {
        print "$var = [ \"\"";
    } else {
        print "$var = [ 0.0";
    }
    for (my $n = 1; $n < $count; $n++) {
        $var = $data->[$n][$m];
        $var = "" if ($var eq "nodata");
        if ($m == 0) {
            print ", $var";
        } elsif (($m==1) || ($m ==2) || ($m == 8) || ($m==15)) {
            print ", \"$var\"";
        } else {
            printf ", %f ", $var;
        }
    }
    print "]\n"
} 

close($fin)
