import FWCore.ParameterSet.Config as cms

process = cms.Process("SKIM")

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_v13', '')

process.source = cms.Source ("PoolSource",
		fileNames = cms.untracked.vstring(
			'file:54C94D12-C4A9-E511-9A60-02163E0138C9.root'
			)
		)

process.maxEvents = cms.untracked.PSet(
		input = cms.untracked.int32 (-1)
		)

import HLTrigger.HLTfilters.hltHighLevel_cfi

process.hltFilterBot005Cent1030 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltFilterBot005Cent1030.HLTPaths = [
		"HLT_HIQ2Bottom005_Centrality1030_v*",
		]

process.hltFilterTop005Cent1030 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltFilterTop005Cent1030.HLTPaths = [
		"HLT_HIQ2Top005_Centrality1030_v*",
		]

process.hltFilterBot005Cent3050 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltFilterBot005Cent3050.HLTPaths = [
		"HLT_HIQ2Bottom005_Centrality3050_v*",
		]

process.hltFilterTop005Cent3050 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltFilterTop005Cent3050.HLTPaths = [
		"HLT_HIQ2Top005_Centrality3050_v*",
		]

process.hltFilterBot005Cent5070 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltFilterBot005Cent5070.HLTPaths = [
		"HLT_HIQ2Bottom005_Centrality5070_v*",
		]

process.hltFilterTop005Cent5070 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltFilterTop005Cent5070.HLTPaths = [
		"HLT_HIQ2Top005_Centrality5070_v*",
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
		process.hltFilterBot005Cent1030
		* process.eventSelection
		* process.centralityBin
		)

import EventContent

process.Out = cms.OutputModule("PoolOutputModule",
		SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')),
		outputCommands = EventContent.analysisSkimQ2Debug.outputCommands,
		fileName = cms.untracked.string ("Q2.root"),
		)

process.out = cms.EndPath(process.Out)
