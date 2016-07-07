//////////////////////////////////////////////////////////
//
//  AccLab UI : simul.js
//
// Copyright (C) 2016 Walid Benghabrit
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
//////////////////////////////////////////////////////////

function command(doc, fx) {
    fx.__doc__ = doc;
    return fx;
}

visualEditor.ui.simul = {
    simulation: null,

    startSimulation: function() {
        this.simulation = {actors: []};
        // TODO
        // 1. Analyse current ACD file and extract all actors with policies
    },

    stopSimulation: function() {
        // TODO close all terminals
        this.simulation = null;
    },

    SimulationCommands: {

        ll: function () {
            //SimulationCommands.ls.call(this, arguments);
        },

        help: command(
            "Show help",
            function(cmd) {
                if(arguments.length > 0) {
                    if(visualEditor.ui.simul.SimulationCommands.hasOwnProperty(cmd)) {
                        this.write(cmd + ' ' + visualEditor.ui.simul.SimulationCommands[cmd].__doc__);
                    } else
                        this.write('Command not found ! Press < tab > to see a list of available commands.');
                }  else
                    this.write('Press < tab > to see a list of available commands.');
                this.exit();
            }),

        policy: command(
            "Show AAL policy attached to the actor",

            function() {
                this.write('AAL policy');
                this.exit();
            }),

        attach: command(
            "Attach the policy 'policy' to the agent",
            function(policy) {
                this.write('new policy');
                this.exit();
            }),

        kv: command(
            "Show local monitor's knowledge vector",
            function() {
                this.write('Local KV');
                this.exit();
            }),

        call: command(
            "Perform a service call by the agent",
            function(action) {
                this.write('calling:' + action);
                this.exit();
            }),

        exit: command("Close the terminal",
                function() {
                // TODO close window
            }),

        sum: function(op1, op2) {
            //if (arguments.length < 2)
            this.exit();
        },

        echo: function() {
            var args = Array.prototype.slice.call(arguments, 0);
            this.write(args.join(' '));

            this.exit(0);
        }
    },

    /**
     * Show actor's console
     * @param actor
     */
    showConsole: function(actor) {
        // Check if simulation is running
        if(visualEditor.ui.simul.simulation == null) {
            toastr.error("No simulation is running !");
            return;
        }

        var target = '.terminal-app-'+actor;
        // Avoid multiple terminals for same actor
        if($(target).length > 0)
            return;

        $("body").append("<div class='terminal-app-"+actor+"'></div>");
        var terminalWin = visualEditor.wm.createWindow.fromQuery(target, {
            title: actor,
            x: 60,
            y: 50,
            width: 500,
            height: 300,
            classname: 'terminal-window',
            widget: false,
            titlebar: true,
            events: {
                closed: function() {
                    this.destroy();
                }
            }
        });

        terminalWin.signals.on('click', function(win){
			terminal.display.focus();
		});

        var terminal = new Terminus(target, {
				welcome: "<div class='identity'><h1>Welcome to " +actor+ "'s shell</h1></div>"+
                "Press <span style='color:green'>&lt; tab &gt;</span> " + "to see a list of available commands."
			});
        terminal.shell.include([this.SimulationCommands]);

		terminal.display.events.on('prompt', function() {
			terminalWin.$content.animate({
				scrollTop:terminalWin.el.find('.terminusjs').height()
			}, 300);
		});

        // Configure the terminal with actor environment
        this.simulation.actors = {
            terminalWin: terminalWin
        };

        // Open the terminal
        terminalWin.open();
    }
};
