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
    monitor_port: 9999,
    currentTerminal: null,

    Actor: function(agent, time, location) {
        return {
            name: agent,
            terminal: null,
            aal_policy: "",
            monitors: [],
            kv: [],
            data: [],
            trace: [],
            violations: [],
            location: "",
            time: "",

            monitor: function() {
                return 0;
            },

            register: function() {
                return 0;
            },

            disableMonitor: function() {
                return 0;
            },

            getKV: function() {
                return 0;
            },

            updateKV: function() {
                return 0;
            },

            pushEvent: function() {
                return 0;
            }
        }
    },

    Data: function(name, types) {
        return {name: name, types: types}
    },

    startSimulation: function(port) {
        visualEditor.ui.simul.monitor_port = port;
        this.simulation = {actors: {}};

        // 1. Analyse current ACD file and extract all actors with policies
        var actors = visualEditor.ui.canvas.getFigures().data.filter(function(e){return e.type === "Actor"});
        var clauses = visualEditor.ui.canvas.getFigures().data.filter(function(e){return e.type === "Policy"});
        for(var i=0; i<actors.length; i++) {
            var agent = actors[i].getName();
            this.simulation.actors[agent] = this.Actor(agent);
        }
    },

    stopSimulation: function() {
        // TODO close all terminals
        this.simulation = null;
    },

    SimulationCommands: {

        ll: function () {
            //SimulationCommands.ls.call(this, arguments);
        },

        sum: function(op1, op2) {
            //if (arguments.length < 2)
            this.exit();
        },

        echo: function() {
            var args = Array.prototype.slice.call(arguments, 0);
            this.write(args.join(' '));

            this.exit(0);
        },

        exit: command(
            "Close the terminal",
            function() {
                this.write('exit');
                this.exit();
            }),

        spoof: command(
            "Spoof an agent id to perform an action.\n Usage: spoof actor_name action",
            function(actor, action) {
                this.write('Spoof');
                this.exit();
            }),

        set_time: command(
            "Change actor's time.\n -Usage: time time" +
            "\n Examples:" +
            "\n - time 3   // Set current actor's location to france",
            function() {
                this.write('Set time');
                this.exit();
            }),

        time: command(
            "Show actor's local time.\n -Usage: time [actor_name]" +
            "\n Examples:" +
            "\n - time     // Show current actor's time"+
            "\n - time bob // Show bob's time",
            function() {
                this.write('Time');
                this.exit();
            }),

        set_location: command(
            "Change actor's location.\n -Usage: location location_name" +
            "\n Examples:" +
            "\n - location  france   // Set current actor's location to france",
            function() {
                this.write('Set location');
                this.exit();
            }),

        location: command(
            "Show actor's location.\n -Usage: location [actor_name]" +
            "\n Examples:" +
            "\n - location     // Show current actor's location"+
            "\n - location bob // Show bob's location",
            function() {
                this.write('location');
                this.exit();
            }),

        violations: command(
            "Show actor violations.",
            function() {
                this.write('Violations');
                this.exit();
            }),

        kv: command(
            "Show local monitor's knowledge vector",
            function() {
                this.write('Local KV');
                this.exit();
            }),

        trace: command(
            "Show actor trace.",
            function() {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                this.write(visualEditor.ui.simul.simulation.actors[actor].trace);
                this.exit();
            }),

        monitor: command(
            "Enable/disable the reference monitor.\n Usage: monitor on/off",
            function() {
                this.write('Monitoring');
                this.exit();
            }),

        call: command(
            "Perform a service call by the agent.\n -Usage: call service[actor](args)",
            function(action) {
                // TODO check with regexp
                var service = action.substring(0, action.indexOf("["));
                var target = action.substring(action.indexOf("[")+1, action.indexOf("]"));
                var args = action.substring(action.indexOf("(")+1, action.indexOf(")"));
                if(args == "") args = "NONE";

                var actor = visualEditor.ui.simul.currentTerminal.agent;
                var currentActorUI = visualEditor.ui.canvas.getFigures().data.filter(
                    function(e){return e.type === "Actor" && e.getName() == actor});
                var targetActorUI = visualEditor.ui.canvas.getFigures().data.filter(
                    function(e){return e.type === "Actor" && e.getName() == target});
                if(currentActorUI.length > 0 && targetActorUI.length > 0) {
                    currentActorUI = currentActorUI[0];
                    targetActorUI = targetActorUI[0];
                    var s1 = currentActorUI.RSO.data.filter(function (e) {
                        return e.text == service
                    });
                    var s2 = targetActorUI.PSO.data.filter(function (e) {
                        return e.text == service
                    });
                    if (s1.length > 0 && s2.length > 0) {
                        var cons = s1[0].getConnections();
                        // TODO select the correct connexion
                        if (cons.data.length > 0) {
                            var old_color = cons.get(0).getColor();
                            cons.get(0).setColor("#230990");
                            // 1. Animate connection
                        }
                    }

                    // 2. Log the event in current actor trace
                    visualEditor.ui.simul.simulation.actors[actor].trace.push(service+"("+actor+","+target+","+args+")");

                    // 3. Send log to monitor

                    // 4. Simulate the network

                    // 5. Log the event in target actor trace

                    // 6. Send log to target's monitor

                    this.write('calling:' + service + " on " + target + " with " + args);
                    this.exit();
                    return;
                }
                this.write("Error actors not found !");
                this.exit();
            }),

        rm: command(
            "Remove a local data.\n - Usage: rm data_name",
            function(name) {
                this.write('removing:' + name);
                this.exit();
            }),

        show_data: command(
            "Show local data of an actor. If actor_name is not specified it shows current actor data" +
            "\nUsage: show_data [actor name]",
            function(name) {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                var data = visualEditor.ui.simul.simulation.actors[actor].data;
                for(var i=0; i<data.length; i++)
                    this.write(data[i].name + ':' + data[i].types + '\n');
                this.exit();
            }),

        data: command(
            "Create a local data. Usage: data name type1 type2 ... typeN",
            function(name) {
                if(name != undefined) {
                    // TODO check if data exsits
                    var actor = visualEditor.ui.simul.currentTerminal.agent;
                    var types = [];
                    if(arguments.length > 1)
                        types = Array.prototype.slice.call(arguments, 0).slice(1);
                    var d = visualEditor.ui.simul.Data(name, types);
                    visualEditor.ui.simul.simulation.actors[actor].data.push(d);
                    this.write('Data stored ! ');
                } else
                    this.write('Error no name given! ');
                this.exit();
            }),

        attach: command(
            "Attach the policy 'policy' to the agent.",
            function(policy) {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                var clauses = visualEditor.ui.canvas.getFigures().data.filter(
                    function(e){return e.type === "Policy" && e.tlabel.text == policy});
                if(clauses.length > 0) {
                    visualEditor.ui.simul.simulation.actors[actor].aal_policy = policy;
                    this.write("Policy " + policy + " attached successfully !");
                } else
                    this.write("Error: policy " + policy + " not found !");
                this.exit();
            }),

        policy: command(
            "Show AAL policy attached to the current actor.",
            function() {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                var policy = visualEditor.ui.simul.simulation.actors[actor].aal_policy;
                var clauses = visualEditor.ui.canvas.getFigures().data.filter(
                    function(e){return e.type === "Policy" && e.tlabel.text == policy});
                if(clauses.length > 0)
                    this.write(clauses[0].policy);
                else
                    this.write("Error: policy " + policy + " not found !");
                this.exit();
            }),

        policy_name: command(
            "Show AAL policy name attached to the current actor.",
            function() {
                var actor = visualEditor.ui.simul.currentTerminal.agent;
                var policy = visualEditor.ui.simul.simulation.actors[actor].aal_policy;
                this.write(policy);
                this.exit();
            }),

        help: command(
            "Show help",
            function(cmd) {
                if(arguments.length > 0) {
                    if(visualEditor.ui.simul.SimulationCommands.hasOwnProperty(cmd)) {
                        this.write(visualEditor.ui.simul.SimulationCommands[cmd].__doc__);
                    } else
                        this.write('Command not found ! Press < tab > to see a list of available commands.');
                }  else
                    this.write('Press < tab > to see a list of available commands.');
                this.exit();
            })
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
            visualEditor.ui.simul.currentTerminal = terminal;
		});

        var terminal = new Terminus(target, {
				welcome: "<div class='identity'><h1>Welcome to " +actor+ "'s shell</h1></div>"+
                "Press <span style='color:green'>&lt; tab &gt;</span> " + "to see a list of available commands."
			});
        terminal.shell.include([this.SimulationCommands]);
        terminal.agent = actor;

		terminal.display.events.on('prompt', function() {
			terminalWin.$content.animate({
				scrollTop:terminalWin.el.find('.terminusjs').height()
			}, 300);
		});

        // Configure the terminal with actor environment
        //this.simulation.actors = {
        //    terminalWin: terminalWin
        //};

        // Open the terminal
        terminalWin.open();
    }
};
