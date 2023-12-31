import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.rerecoRho_cff import *
from HeavyIonsAnalysis.JetAnalysis.rerecoJets_cff import *
from HeavyIonsAnalysis.JetAnalysis.rerecoTracks_cff import *

from HeavyIonsAnalysis.JetAnalysis.jets.ak4PFJetSequence_pponPbPb_data_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.ak2PFJetSequence_pponPbPb_data_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.ak6PFJetSequence_pponPbPb_data_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.ak8PFJetSequence_pponPbPb_data_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akSoftDrop4PFJetSequence_pponPbPb_data_cff import *

from HeavyIonsAnalysis.JetAnalysis.jets.akPu3CaloJetSequence_pponPbPb_data_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_pponPbPb_data_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akCs3PFJetSequence_pponPbPb_data_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akFlowPuCs3PFJetSequence_pponPbPb_data_cff import *

from HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_pponPbPb_data_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_pponPbPb_data_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akCs4PFJetSequence_pponPbPb_data_cff import *
from HeavyIonsAnalysis.JetAnalysis.jets.akFlowPuCs4PFJetSequence_pponPbPb_data_cff import *

jetSequence = cms.Sequence(
    rhoSequence +

    highPurityTracks +

    akPu3CaloJets +
    akPu3PFJets +
    akCs3PFJets +
    akFlowPuCs3PFJets +

    akPu4CaloJets +
    akPu4PFJets +
    akCs4PFJets +
    akFlowPuCs4PFJets +
    ak4PFJets +
 
    ak2PFJets +
    ak6PFJets +    
    ak8PFJets +
    akSoftDrop4PFJets +

    akPu3CaloJetSequence +
    akPu3PFJetSequence +
    akCs3PFJetSequence +
    akFlowPuCs3PFJetSequence +

    akPu4CaloJetSequence +
    akPu4PFJetSequence +
    akCs4PFJetSequence +
    akFlowPuCs4PFJetSequence +
    ak2PFJetSequence +
    ak6PFJetSequence +
    ak8PFJetSequence +
    akSoftDrop4PFJetSequence +
    ak4PFJetSequence 
)
