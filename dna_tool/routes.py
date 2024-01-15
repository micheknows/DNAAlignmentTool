from flask import Blueprint, render_template, request, flash, redirect, url_for
from DNAAlignmentTool import dna_tool

@dna_tool.route('/test')
def test():
    return "DNA Blueprint Works!"
