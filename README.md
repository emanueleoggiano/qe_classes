# qe_classes

## Motivation
This project was born after I've learned how to write basic Quantum ESPRESSO input file. Tired of having to write very similar code for different projects, I thought it would be better to develop different classes to do this work more quickly and efficiently. For this reason, I created qe_classes, which encapsulates several classes for inputs.

## Developed Class(es)
- `pwx_input`: generate input file for the pw.x program (TO BE COMPLETED)


## Future updates
- [ ] Complete the `pwx_input` class
- [ ] Create a `phx_input` class to create input files for the ph.x program
- [ ] Create classes for the output files

### Future updates for the `pwx_input` class
- [ ] Update the two methods that contains pass inside them
- [ ] Add the `ATOMIC_SPECIES` method
- [ ] Add the `ATOMIC_POSITIONS` method
- [ ] Add the preview method in order to see how to code will be written in the .in file before creating it
- [ ] Add the write method in order to write the complete .in file
- [ ] Add run method to execute the file
- [ ] Add the `K_POINTS` method

## Lates Updates
- [ ] Added the `prepare` method in `ipwx` class
