#Stacked Autodenoising Autoencoders

Stacked Autodenoising Autoencoders (SDAs) were used to create a patient representation for the purposes of predicting diagnoses.

## Hyper Parameter Selection
3 layers stack of denoising autoencoders (layers produce no obvious improvement)
500 hidden units per layer
5% noise corruption factor (used zero-out masking noise)
Sigmoid activation function
100 random forest trees
