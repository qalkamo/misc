package MyModuleBuilder;
use Module::Build;
@ISA = qw(Module::Build);
    sub process_c_bin_files {
	my $self = shift;
	chomp(my $make  = `which make`);
	chomp(my $nmake = `which nmake`);
	$make ||= $nmake;
	system "cd c_bin; $make INCLUDES=-I../samtools-0.1.17 LIBPATH=-L../samtools-0.1.17";
	mkdir "blib/bin" unless -e "blib/bin";
        my @exec = grep {-x $_} <c_bin/*>;
	$self->copy_if_modified(from   =>$_,
				 to_dir => "./blib/bin/",
				 flatten=>1,
	    ) foreach @exec;
    }

    sub ACTION_clean {
	my $self = shift;
	$self->SUPER::ACTION_clean();
        system "cd c_bin; make -s clean";
    }

1;
