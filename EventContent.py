import FWCore.ParameterSet.Config as cms

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

        # tower
        'keep recoCastorTowers_CastorTowerReco_*_*',

        # jet
        'keep *_towerMaker_*_*',

        # vertex
        'keep *_hiSelectedVertex_*_*',

        # full tracks
        'keep recoTracks_hiGeneralTracks_*_*',
        )
)


