#!/usr/bin/perl
#Course:  CSCI 6509
#Author: Viswanath MuthuKumaraSwamy Sathananth
#Description: Solution for - Program reads two inputs from command line
#	      checks for the first input in the file given as second input. 
#             Prints the word before and after each match

#Subroutine to print according to the format provided in the assignment
#Control is at a single point.
sub print_format{
	printf("%12s %s %s\n",$_[0],$_[1],$_[2]);
}
my $match_word = lc (shift);#first parameter represents the word.
chmod $match_word;
my $file_name = shift;#second parameter represents the filename
my @word_array = ('START');#Starting with a start in the array.
open(my $fh,'<',$file_name) or die "Cannot open file $file_name $!";
while(<$fh>){
	while(/[a-zA-Z0-9_]+/g){
		push @word_array, lc($&);
		if(scalar(@word_array)> 3){
			shift @word_array;
		}
		if(scalar(@word_array) == 3){
			if($word_array[1] eq $match_word){
				&print_format(@word_array);
			}
		}
	}
}
#To handle the end case. Checking the last trigram.
if($word_array[2] eq $match_word){
      shift @word_array;
      push @word_array, 'END';
      &print_format(@word_array);
}
