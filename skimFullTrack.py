import FWCore.ParameterSet.Config as cms

process = cms.Process("SKIM")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data_HIon', '')

process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring(
                                     'file:HardProbe1.root'
#                                     'file:../tmp/AOD/12336140-3999-E511-8C97-02163E01439B.root' #HIMinimumBias1
#                                     '/store/express/HIRun2015/HIExpressPhysics/FEVT/Express-v1/000/262/921/00000/FC979710-9097-E511-A28B-02163E013523.root'
                             )
                            )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32 (-1)
)

import HLTrigger.HLTfilters.hltHighLevel_cfi

process.hltFilter = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltFilter.HLTPaths = [
                "HLT_HIFullTrack*",
]


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
        * process.centralityBin
)

import EventContent

process.Out = cms.OutputModule("PoolOutputModule",
                               SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')),
                               outputCommands = EventContent.analysisSkimContent.outputCommands,
                               fileName = cms.untracked.string ("FullTrack.root"),
                              )

process.out = cms.EndPath(process.Out)
