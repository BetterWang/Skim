import FWCore.ParameterSet.Config as cms

process = cms.Process("SKIM")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

#from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data_HIon', '')

process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring(
                                     '/store/express/HIRun2015/HIExpressPhysics/FEVT/Express-v1/000/262/921/00000/FC979710-9097-E511-A28B-02163E013523.root'
                             )
                            )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32 (-1)
)

import HLTrigger.HLTfilters.hltHighLevel_cfi

process.hltFilter = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltFilter.HLTPaths = [
                "HLT_HIL1MinimumBiasHF1AND_v*",
]

analysisSkimContent = cms.PSet(
        outputCommands = cms.untracked.vstring(
        'drop *',
        # event
        'keep *_offlineBeamSpot_*_*',
        'keep *_TriggerResults_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*RECO',

        # centrality
        'keep *_hiCentrality_*_*',
        'keep *_centralityBin_*_*',
        'keep *_hiEvtPlane_*_*',

        # digis
        'keep ZDCDataFramesSorted_castorDigis_*_*',

        # jet
        'keep *_towerMaker_*_*',

        # vertex
        'keep *_hiSelectedVertex_*_*',

        # full tracks
#        'keep recoTracks_hiGeneralAndPixelTracks_*_*',
        'keep recoTracks_hiGeneralTracks_*_*',
        )
)

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")


process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.clusterCompatibilityFilter.clusterPars = cms.vdouble(0.0,0.006)

process.eventSelection = cms.Sequence(
        process.hfCoincFilter3
        + process.primaryVertexFilter
        + process.clusterCompatibilityFilter
)

process.p = cms.Path(
        process.hltFilter
        * process.eventSelection
)


process.Out = cms.OutputModule("PoolOutputModule",
                               SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')),
                               outputCommands = analysisSkimContent.outputCommands,
                               fileName = cms.untracked.string ("HIExpressMB.root"),
                              )

process.out = cms.EndPath(process.Out)
