itk_module_test()

set( RLEImageTests
        itkRLEImageTest.cxx
        itkRegionOfInterestRLEImageFilterTest.cxx
        itkIteratorTestsForRLEImage.cxx
        itkRLEImageIteratorsForwardBackwardTest.cxx
        itkRLEImageIteratorTest.cxx
        itkRLEImageIteratorWithIndexTest.cxx
        itkRLEImageRegionConstIteratorWithOnlyIndexTest.cxx
        itkRLEImageRegionIteratorTest.cxx
        itkRLEImageScanlineIteratorTest1.cxx)

CreateTestDriver( RLEImage "${RLEImage-Test_LIBRARIES}" "${RLEImageTests}" )

add_executable(runFromIDE manualTest.cxx ${RLEImageTests})
target_link_libraries(runFromIDE ${RLEImage-Test_LIBRARIES})

add_executable(rleStats rleStats.cxx)
target_link_libraries(rleStats ${RLEImage-Test_LIBRARIES})

itk_add_test( NAME itkIteratorTestsForRLEImage COMMAND RLEImageTestDriver itkIteratorTestsForRLEImage)
itk_add_test( NAME itkRegionOfInterestRLEImageFilterTest COMMAND RLEImageTestDriver itkRegionOfInterestRLEImageFilterTest)
itk_add_test( NAME itkRLEImageIteratorsForwardBackwardTest COMMAND RLEImageTestDriver itkRLEImageIteratorsForwardBackwardTest)
itk_add_test( NAME itkRLEImageIteratorTest COMMAND RLEImageTestDriver itkRLEImageIteratorTest itkRLEImageIteratorWithIndexTest)
itk_add_test( NAME itkRLEImageIteratorWithIndexTest COMMAND RLEImageTestDriver itkRLEImageIteratorWithIndexTest)
itk_add_test( NAME itkRLEImageRegionConstIteratorWithOnlyIndexTest COMMAND RLEImageTestDriver itkRLEImageRegionConstIteratorWithOnlyIndexTest)
itk_add_test( NAME itkRLEImageRegionIteratorTest COMMAND RLEImageTestDriver itkRLEImageRegionIteratorTest)
itk_add_test( NAME itkRLEImageScanlineIteratorTest1 COMMAND RLEImageTestDriver itkRLEImageScanlineIteratorTest1)


function(ReadWriteTest ImageName Ext) # optional: big
  set(outImage "${ITK_TEST_OUTPUT_DIR}/${ImageName}.${Ext}")
  if ("${ARGN}" STREQUAL "big")
    if (DEFINED ITK_COMPUTER_MEMORY_SIZE)
      if (${ITK_COMPUTER_MEMORY_SIZE} GREATER_EQUAL 16)
        itk_add_test( NAME RLEImage${ImageName}
          COMMAND RLEImageTestDriver
          --compare DATA{Input/${ImageName}.${Ext}} ${outImage}
          itkRLEImageTest
            DATA{Input/${ImageName}.${Ext}} ${outImage})
        set_property(TEST RLEImage${ImageName} APPEND PROPERTY LABELS RUNS_LONG)
        set_property(TEST RLEImage${ImageName} APPEND PROPERTY RUN_SERIAL True)
      endif()
    endif()
  else()
    itk_add_test( NAME RLEImage${ImageName}
      COMMAND RLEImageTestDriver
      --compare DATA{Input/${ImageName}.${Ext}} ${outImage}
      itkRLEImageTest
        DATA{Input/${ImageName}.${Ext}} ${outImage})
  endif()
endfunction()

# RLEImage specific tests - quick
ReadWriteTest(Small2D png)
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
ReadWriteTest(wb-seg nrrd big)
ReadWriteTest(wb-seg32 nrrd big)
