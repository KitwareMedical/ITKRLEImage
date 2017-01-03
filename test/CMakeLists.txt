itk_module_test()

set( RLEImageTests itkRLEImageTest.cxx )

CreateTestDriver( RLEImage "${RLEImage-Test_LIBRARIES}" "${RLEImageTests}" )

add_executable(runFromIDE manualTest.cxx ${RLEImageTests})
target_link_libraries(runFromIDE ${RLEImage-Test_LIBRARIES})

add_executable(rleStats rleStats.cxx)
target_link_libraries(rleStats ${RLEImage-Test_LIBRARIES})

ADD_EXECUTABLE(iteratorTests
    itkRegionOfInterestImageFilterTest.cxx
    itkIteratorTests.cxx
    itkImageIteratorsForwardBackwardTest.cxx
    itkImageIteratorTest.cxx
    itkImageIteratorWithIndexTest.cxx
    itkImageRegionConstIteratorWithOnlyIndexTest.cxx
    itkImageRegionIteratorTest.cxx
    itkImageScanlineIteratorTest1.cxx
    iteratorTests.cxx)
TARGET_LINK_LIBRARIES(iteratorTests "${RLEImage-Test_LIBRARIES}")
itk_add_test( NAME RLEImageiteratorTests COMMAND iteratorTests)

function(ReadWriteTest ImageName Ext)
  set(outImage "${ITK_TEST_OUTPUT_DIR}/${ImageName}.${Ext}")
  itk_add_test( NAME RLEImage${ImageName}
    COMMAND RLEImageTestDriver
    --compare DATA{Input/${ImageName}.${Ext}} ${outImage}
    itkRLEImageTest
      DATA{Input/${ImageName}.${Ext}} ${outImage})
endfunction()

# RLEImage specific tests - quick
ReadWriteTest(brainParc mha)
ReadWriteTest(vb-seg mha)
ReadWriteTest(ws nrrd)
ReadWriteTest(wb-crop nrrd)

# Handcrafted tests for MorphologicalContourInterpolation
ReadWriteTest(Empty nrrd)
ReadWriteTest(NoSlices nrrd)
ReadWriteTest(Micro1 nrrd)
ReadWriteTest(SimplestOneToOne nrrd)
ReadWriteTest(OneToOne nrrd)
ReadWriteTest(OneToThree nrrd)
ReadWriteTest(ExtrapolationAppearing nrrd)
ReadWriteTest(DoubleTwoLabelBranching nrrd)
ReadWriteTest(TwoAxisDoubleTwoLabelBC nrrd)
ReadWriteTest(AccidentalMiddleSliceSeg nrrd)
ReadWriteTest(ThreeAxisFourLabelConflict nrrd)
ReadWriteTest(SevenLabels nrrd)
ReadWriteTest(FullEnd nrrd)
ReadWriteTest(1MN1 nrrd)
ReadWriteTest(ManyToMany16 nrrd)
ReadWriteTest(ManyToMany nrrd)
ReadWriteTest(GridSeg nrrd)
ReadWriteTest(GridSeg2 nrrd)
ReadWriteTest(FourD nrrd)
ReadWriteTest(2D png)
ReadWriteTest(BigZ nrrd)
ReadWriteTest(FaceRoI nrrd)

# Paul's test images
ReadWriteTest(105769moving nii.gz)
ReadWriteTest(105769fixed nii.gz)
ReadWriteTest(64816L_amygdala_fin nii.gz)
ReadWriteTest(64816L_amygdala_int nii.gz)
ReadWriteTest(65239R_amygdala_fin nii.gz)
ReadWriteTest(65239R_amygdala_int nii.gz)

# RLEImage specific tests - long
ReadWriteTest(wb-seg nrrd)
ReadWriteTest(wb-seg32 nrrd)
