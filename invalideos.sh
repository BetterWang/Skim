#python $DBS3_CLIENT_ROOT/examples/DBS3SetFileStatus.py --url=https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter --status=invalid --recursive=False  --files=/store/group/phys_heavyions/qwang/HIHardProbes/HIHardProbes_FullTrackSkim2015/151210_124927/0000/FullTrack_19.root
python $DBS3_CLIENT_ROOT/examples/DBS3SetDatasetStatus.py --dataset=/HIHardProbes/qwang-HIHardProbes_FullTrackSkim2015_v2-82d3c5ee469522058df894563cd74923/USER --url=https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter --status=INVALID --recursive=False
