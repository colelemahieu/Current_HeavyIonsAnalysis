import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.HiReRecoJets_HI_cff import PFTowers, kt4PFJets, hiFJRhoProducer, hiFJGridEmptyAreaCalculator, ak4PFJets

#jet analyzers
from HeavyIonsAnalysis.JetAnalysis.jets.ak4PFJetSequence_PbPb_jec_cff import *

highPurityTracks = cms.EDFilter("TrackSelector",
                                src = cms.InputTag("hiGeneralTracks"),
                                cut = cms.string('quality("highPurity")'))

from RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi import *
offlinePrimaryVertices.TrackLabel = 'highPurityTracks'




jetSequences = cms.Sequence(
    PFTowers + 
    kt4PFJets +
    hiFJRhoProducer +
    hiFJGridEmptyAreaCalculator + 

    ak4PFJets +

    
    highPurityTracks +
    offlinePrimaryVertices +

    ak4PFJetSequence 

)
