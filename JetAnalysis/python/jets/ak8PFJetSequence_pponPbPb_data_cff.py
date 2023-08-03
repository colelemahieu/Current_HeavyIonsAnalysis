import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

ak8PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("ak8PFJets"),
    matched = cms.InputTag("ak8HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.8
    )

ak8PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak8HiSignalGenJets"),
    matched = cms.InputTag("ak8HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.8
    )

ak8PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("ak8PFJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

ak8PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative','L2L3Residual'),
    src = cms.InputTag("ak8PFJets"),
    payload = "AK8PF"
    )

ak8PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('ak8CaloJets'))

# ak6PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak6HiSignalGenJets'))

ak8PFbTagger = bTaggers(
    "ak8PF",
    0.8)

# create objects locally since they dont load properly otherwise
ak8PFPatJetPartons = ak8PFbTagger.PatJetPartons
ak8PFJetTracksAssociatorAtVertex = ak8PFbTagger.JetTracksAssociatorAtVertex
ak8PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
ak8PFSimpleSecondaryVertexHighEffBJetTags = ak8PFbTagger.SimpleSecondaryVertexHighEffBJetTags
ak8PFSimpleSecondaryVertexHighPurBJetTags = ak8PFbTagger.SimpleSecondaryVertexHighPurBJetTags
ak8PFCombinedSecondaryVertexBJetTags = ak8PFbTagger.CombinedSecondaryVertexBJetTags
ak8PFCombinedSecondaryVertexV2BJetTags = ak8PFbTagger.CombinedSecondaryVertexV2BJetTags
ak8PFJetBProbabilityBJetTags = ak8PFbTagger.JetBProbabilityBJetTags
ak8PFSoftPFMuonByPtBJetTags = ak8PFbTagger.SoftPFMuonByPtBJetTags
ak8PFSoftPFMuonByIP3dBJetTags = ak8PFbTagger.SoftPFMuonByIP3dBJetTags
ak8PFTrackCountingHighEffBJetTags = ak8PFbTagger.TrackCountingHighEffBJetTags
ak8PFTrackCountingHighPurBJetTags = ak8PFbTagger.TrackCountingHighPurBJetTags

ak8PFImpactParameterTagInfos = ak8PFbTagger.ImpactParameterTagInfos
ak8PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
ak8PFJetProbabilityBJetTags = ak8PFbTagger.JetProbabilityBJetTags

ak8PFSecondaryVertexTagInfos = ak8PFbTagger.SecondaryVertexTagInfos
ak8PFSimpleSecondaryVertexHighEffBJetTags = ak8PFbTagger.SimpleSecondaryVertexHighEffBJetTags
ak8PFSimpleSecondaryVertexHighPurBJetTags = ak8PFbTagger.SimpleSecondaryVertexHighPurBJetTags
ak8PFCombinedSecondaryVertexBJetTags = ak8PFbTagger.CombinedSecondaryVertexBJetTags
ak8PFCombinedSecondaryVertexV2BJetTags = ak8PFbTagger.CombinedSecondaryVertexV2BJetTags

ak8PFSecondaryVertexNegativeTagInfos = ak8PFbTagger.SecondaryVertexNegativeTagInfos
ak8PFNegativeSimpleSecondaryVertexHighEffBJetTags = ak8PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
ak8PFNegativeSimpleSecondaryVertexHighPurBJetTags = ak8PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
ak8PFNegativeCombinedSecondaryVertexBJetTags = ak8PFbTagger.NegativeCombinedSecondaryVertexBJetTags
ak8PFPositiveCombinedSecondaryVertexBJetTags = ak8PFbTagger.PositiveCombinedSecondaryVertexBJetTags
ak8PFNegativeCombinedSecondaryVertexV2BJetTags = ak8PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
ak8PFPositiveCombinedSecondaryVertexV2BJetTags = ak8PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

ak8PFSoftPFMuonsTagInfos = ak8PFbTagger.SoftPFMuonsTagInfos
ak8PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
ak8PFSoftPFMuonBJetTags = ak8PFbTagger.SoftPFMuonBJetTags
ak8PFSoftPFMuonByIP3dBJetTags = ak8PFbTagger.SoftPFMuonByIP3dBJetTags
ak8PFSoftPFMuonByPtBJetTags = ak8PFbTagger.SoftPFMuonByPtBJetTags
ak8PFNegativeSoftPFMuonByPtBJetTags = ak8PFbTagger.NegativeSoftPFMuonByPtBJetTags
ak8PFPositiveSoftPFMuonByPtBJetTags = ak8PFbTagger.PositiveSoftPFMuonByPtBJetTags
ak8PFPatJetFlavourAssociation = ak8PFbTagger.PatJetFlavourAssociation
ak8PFPatJetFlavourId = cms.Sequence(ak8PFPatJetPartons*ak8PFPatJetFlavourAssociation)

ak8PFJetBtaggingIP = cms.Sequence(
    ak8PFImpactParameterTagInfos *
    ak8PFTrackCountingHighEffBJetTags +
    ak8PFTrackCountingHighPurBJetTags +
    ak8PFJetProbabilityBJetTags +
    ak8PFJetBProbabilityBJetTags
    )

ak8PFJetBtaggingSV = cms.Sequence(
    ak8PFImpactParameterTagInfos *
    ak8PFSecondaryVertexTagInfos *
    ak8PFSimpleSecondaryVertexHighEffBJetTags +
    ak8PFSimpleSecondaryVertexHighPurBJetTags +
    ak8PFCombinedSecondaryVertexBJetTags +
    ak8PFCombinedSecondaryVertexV2BJetTags
    )

ak8PFJetBtagging = cms.Sequence(
    ak8PFJetBtaggingIP
    * ak8PFJetBtaggingSV
    # * ak6PFJetBtaggingNegSV
    # * ak6PFJetBtaggingMu
    )

ak8PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("ak8PFJets"),
    genJetMatch            = cms.InputTag("ak8PFmatch"),
    genPartonMatch         = cms.InputTag("ak8PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("ak8PFcorr")),
    JetPartonMapSource     = cms.InputTag("ak8PFPatJetFlavourAssociation"),
    JetFlavourInfoSource   = cms.InputTag("ak8PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("ak8PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = False,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("ak8PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("ak8PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("ak8PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("ak8PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("ak8PFJetBProbabilityBJetTags"),
        cms.InputTag("ak8PFJetProbabilityBJetTags"),
        # cms.InputTag("ak6PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("ak6PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("ak8PFTrackCountingHighEffBJetTags"),
        cms.InputTag("ak8PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("ak8PFImpactParameterTagInfos"),cms.InputTag("ak8PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("ak8PFJetID"),
    addBTagInfo = True,
    addTagInfos = True,
    addDiscriminators = True,
    addAssociatedTracks = True,
    addJetCharge = False,
    addJetID = False,
    getJetMCFlavour = False,
    addGenPartonMatch = False,
    addGenJetMatch = False,
    embedGenJetMatch = False,
    embedGenPartonMatch = False,
    # embedCaloTowers = False,
    # embedPFCandidates = True
    )

ak8PFNjettiness = Njettiness.clone(
    src = cms.InputTag("ak8PFJets"),
    R0  = cms.double(0.8)
    )

ak8PFpatJetsWithBtagging.userData.userFloats.src += [
    'ak8PFNjettiness:tau1',
    'ak8PFNjettiness:tau2',
    'ak8PFNjettiness:tau3']

ak8PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("ak8PFpatJetsWithBtagging"),
    genjetTag = 'ak8HiSignalGenJets',
    rParam = 0.8,
    matchJets = cms.untracked.bool(False),
    matchTag = 'patJetsWithBtagging',
    pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
    trackTag = cms.InputTag("generalTracks"),
    fillGenJets = False,
    isMC = False,
    doSubEvent = False,
    useHepMC = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    eventInfoTag = cms.InputTag("generator"),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    bTagJetName = cms.untracked.string("ak8PF"),
    jetName = cms.untracked.string("ak8PF"),
    genPtMin = cms.untracked.double(5),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(False),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("ak8GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("ak8HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("ak8HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("ak8HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("ak8GenJets","sym"),
    genDroppedBranches = cms.InputTag("ak8GenJets","droppedBranches")
    )

ak8PFJetSequence_mc = cms.Sequence(
    # ak6PFclean
    # *
    ak8PFmatch
    # *
    # ak6PFmatchGroomed
    *
    ak8PFparton
    *
    ak8PFcorr
    # *
    # ak6PFJetID
    *
     ak8PFPatJetFlavourId
    *
    ak8PFJetTracksAssociatorAtVertex
    *
    ak8PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    ak8PFNjettiness
    *
    ak8PFpatJetsWithBtagging
    *
    ak8PFJetAnalyzer
    )


ak8PFJetSequence_data = cms.Sequence(
    ak8PFcorr
    *
    # ak6PFJetID
    # *
    ak8PFJetTracksAssociatorAtVertex
    *
    ak8PFJetBtagging
    *
    ak8PFNjettiness
    *
    ak8PFpatJetsWithBtagging
    *
    ak8PFJetAnalyzer
    )

ak8PFJetSequence_mb = cms.Sequence(
    ak8PFJetSequence_mc)
ak8PFJetSequence_jec = cms.Sequence(
    ak8PFJetSequence_mc)

ak8PFJetSequence = cms.Sequence(
    ak8PFJetSequence_data)
